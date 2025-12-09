import requests
import logging
import time
import random
import schedule
from lxml import etree
from config import (
    HEADERS, POPULAR_VIDEO_URL, VIDEO_DETAIL_URL, DANMAKU_URL,
    get_db_connection, init_database
)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bilibili_crawler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_popular_videos(total=600):
    """
    获取热门视频列表
    :param total: 要获取的视频总数
    :return: 视频列表，每个元素包含bvid
    """
    try:
        bvid_list = []
        page = 1
        page_size = 50  # 每页50个视频
        max_pages = (total + page_size - 1) // page_size  # 计算需要的最大页数
        retry_count = 0
        max_retries = 3
        
        while len(bvid_list) < total and page <= max_pages:
            try:
                params = {
                    'ps': page_size,
                    'pn': page
                }
                response = requests.get(POPULAR_VIDEO_URL, headers=HEADERS, params=params)
                response.raise_for_status()
                
                # 尝试解析JSON
                try:
                    data = response.json()
                except json.JSONDecodeError as json_err:
                    logger.error(f"获取热门视频列表第{page}页失败: JSON解析错误 - {str(json_err)}")
                    logger.error(f"响应内容前500字符: {response.text[:500]}")
                    retry_count += 1
                    if retry_count >= max_retries:
                        logger.error(f"重试次数已达上限，停止获取热门视频")
                        break
                    # 增加延时后重试
                    time.sleep(random.uniform(3.0, 5.0))
                    continue
                
                if data['code'] != 0:
                    logger.error(f"获取热门视频列表第{page}页失败: {data['message']}")
                    page += 1
                    retry_count = 0
                    time.sleep(random.uniform(1.0, 2.0))
                    continue
                
                videos = data['data']['list']
                if not videos:
                    logger.warning(f"获取热门视频列表第{page}页成功，但返回空列表")
                    page += 1
                    retry_count = 0
                    time.sleep(random.uniform(1.0, 2.0))
                    continue
                
                new_bvids = [video['bvid'] for video in videos]
                bvid_list.extend(new_bvids)
                
                logger.info(f"成功获取第{page}页热门视频，累计{len(bvid_list)}个")
                
                page += 1
                retry_count = 0
                # 防止请求过快，添加适当延时
                time.sleep(random.uniform(1.0, 2.0))
                
            except requests.exceptions.RequestException as req_err:
                logger.error(f"获取热门视频列表第{page}页网络请求失败: {str(req_err)}")
                retry_count += 1
                if retry_count >= max_retries:
                    logger.error(f"重试次数已达上限，停止获取热门视频")
                    break
                # 增加延时后重试
                time.sleep(random.uniform(3.0, 5.0))
                continue
        
        # 只返回需要的数量
        bvid_list = bvid_list[:total]
        logger.info(f"成功获取{len(bvid_list)}个热门视频")
        return bvid_list
    
    except Exception as e:
        logger.error(f"获取热门视频列表时发生错误: {str(e)}")
        return bvid_list


def get_video_detail(bvid):
    """
    获取视频详情
    :param bvid: 视频的bvid
    :return: 视频详情字典，包含aid、cid、title、pic_url、total_danmaku等信息
    """
    try:
        params = {
            'bvid': bvid
        }
        response = requests.get(VIDEO_DETAIL_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['code'] != 0:
            logger.error(f"获取视频{bvid}详情失败: {data['message']}")
            return None
        
        video_data = data['data']
        # 处理封面URL，确保使用HTTPS协议
        pic_url = video_data['pic']
        if pic_url.startswith('//'):
            pic_url = 'https:' + pic_url
        elif pic_url.startswith('http://'):
            pic_url = pic_url.replace('http://', 'https://')
        elif not pic_url.startswith('http'):
            pic_url = 'https://' + pic_url
        
        detail = {
            'bvid': video_data['bvid'],
            'aid': video_data['aid'],
            'cid': video_data['cid'],
            'title': video_data['title'],
            'pic_url': pic_url,
            'total_danmaku': video_data['stat']['danmaku']  # 获取弹幕总数
        }
        logger.info(f"成功获取视频{bvid}详情: {detail['title']} (弹幕数: {detail['total_danmaku']})")
        return detail
    
    except Exception as e:
        logger.error(f"获取视频{bvid}详情时发生错误: {str(e)}")
        return None


def analyze_danmaku(cid):
    """
    获取并分析弹幕
    :param cid: 弹幕池ID
    :return: 包含total_danmaku、question_count的字典
    """
    try:
        url = DANMAKU_URL.format(cid=cid)
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        # 解析XML
        root = etree.fromstring(response.content)
        danmaku_list = root.xpath('//d/text()')
        
        total_danmaku = len(danmaku_list)
        question_count = 0
        
        # 统计包含问号的弹幕数量
        for danmaku in danmaku_list:
            if '?' in danmaku or '？' in danmaku:
                question_count += 1
        
        logger.info(f"成功分析弹幕: 总数{total_danmaku}, 问号数量{question_count}")
        return {
            'total_danmaku': total_danmaku,
            'question_count': question_count
        }
    
    except Exception as e:
        logger.error(f"分析弹幕cid={cid}时发生错误: {str(e)}")
        return None


def calculate_confusion_index(total_danmaku, question_count):
    """
    计算疑惑指数
    :param total_danmaku: 弹幕总数
    :param question_count: 包含问号的弹幕数量
    :return: 疑惑指数（保留两位小数）
    """
    if total_danmaku == 0:
        return 0.0
    
    confusion_index = (question_count / total_danmaku) * 100
    return round(confusion_index, 2)


def save_video_stats(video_data, danmaku_stats):
    """
    保存视频统计数据到数据库
    :param video_data: 视频详情字典
    :param danmaku_stats: 弹幕统计字典
    """
    try:
        confusion_index = calculate_confusion_index(
            danmaku_stats['total_danmaku'],
            danmaku_stats['question_count']
        )
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 使用upsert语句，存在则更新，不存在则插入
        cursor.execute('''
            INSERT OR REPLACE INTO video_stats (
                bvid, aid, cid, title, pic_url, total_danmaku, 
                question_count, confusion_index
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            video_data['bvid'],
            video_data['aid'],
            video_data['cid'],
            video_data['title'],
            video_data['pic_url'],
            danmaku_stats['total_danmaku'],
            danmaku_stats['question_count'],
            confusion_index
        ))
        
        conn.commit()
        conn.close()
        
        logger.info(f"成功保存视频{video_data['bvid']}的统计数据")
    
    except Exception as e:
        logger.error(f"保存视频{video_data['bvid']}统计数据时发生错误: {str(e)}")


def generate_rankings(sort_by='question_count', limit=10):
    """
    生成排行榜
    :param sort_by: 排序字段，可选值：question_count（问号数量）、confusion_index（疑惑指数）
    :param limit: 展示的视频数量
    :return: 排行榜数据列表
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 验证排序字段
        if sort_by not in ['question_count', 'confusion_index']:
            sort_by = 'question_count'
        
        cursor.execute(f'''
            SELECT bvid, title, total_danmaku, question_count, confusion_index
            FROM video_stats
            ORDER BY {sort_by} DESC
            LIMIT ?
        ''', (limit,))
        
        rankings = cursor.fetchall()
        conn.close()
        
        logger.info(f"成功生成按{sort_by}排序的Top {limit}排行榜")
        return rankings
    
    except Exception as e:
        logger.error(f"生成排行榜时发生错误: {str(e)}")
        return []


def print_rankings(rankings, sort_by='question_count'):
    """
    打印排行榜
    :param rankings: 排行榜数据列表
    :param sort_by: 排序字段
    """
    if not rankings:
        print("暂无排行榜数据")
        return
    
    print("\n" + "="*80)
    if sort_by == 'question_count':
        print("B站热门视频问号数量排行榜")
    else:
        print("B站热门视频疑惑指数排行榜")
    print("="*80)
    print(f"{'排名':<5} {'标题':<50} {'问号数量':<10} {'疑惑指数':<10} {'弹幕总数':<10}")
    print("-"*80)
    
    for i, rank in enumerate(rankings, 1):
        title = rank['title'][:47] + '...' if len(rank['title']) > 50 else rank['title']
        print(f"{i:<5} {title:<50} {rank['question_count']:<10} {rank['confusion_index']:<10.2f} {rank['total_danmaku']:<10}")
    
    print("="*80 + "\n")


def crawl_videos(total=600):
    """
    执行视频数据采集
    :param total: 要抓取的视频总数
    """
    logger.info("开始执行B站视频数据采集器")
    
    # 初始化数据库
    init_database()
    
    # Step 1: 获取热门视频列表
    bvid_list = get_popular_videos(total)
    if not bvid_list:
        logger.error("未能获取到热门视频列表，程序终止")
        return
    
    # Step 2-4: 遍历视频列表，获取详情、分析弹幕、保存数据
    processed_count = 0
    skipped_count = 0
    
    for bvid in bvid_list:
        # 获取视频详情
        video_detail = get_video_detail(bvid)
        if not video_detail:
            time.sleep(random.uniform(0.5, 1.5))  # 减少延时
            continue
        
        # 检查弹幕总数，少于200的跳过
        if video_detail.get('total_danmaku', 0) < 200:
            logger.info(f"视频{video_detail['title']}弹幕总数{video_detail['total_danmaku']}少于200，跳过分析")
            skipped_count += 1
            time.sleep(random.uniform(0.5, 1.5))  # 减少延时
            continue
        
        # 获取并分析弹幕
        danmaku_stats = analyze_danmaku(video_detail['cid'])
        if not danmaku_stats:
            time.sleep(random.uniform(0.5, 1.5))  # 减少延时
            continue
        
        # 保存数据
        save_video_stats(video_detail, danmaku_stats)
        processed_count += 1
        
        logger.info(f"已处理 {processed_count}/{len(bvid_list)} 个视频，跳过 {skipped_count} 个弹幕数不足的视频")
        
        # 随机延时 - 优化速率
        time.sleep(random.uniform(0.5, 1.5))
    
    # 生成并打印排行榜
    logger.info("开始生成排行榜")
    
    # 按问号数量排序的排行榜
    question_rankings = generate_rankings(sort_by='question_count', limit=10)
    print_rankings(question_rankings, sort_by='question_count')
    
    # 按疑惑指数排序的排行榜
    confusion_rankings = generate_rankings(sort_by='confusion_index', limit=10)
    print_rankings(confusion_rankings, sort_by='confusion_index')
    
    logger.info(f"B站视频数据采集器执行完成，共处理 {processed_count} 个视频，跳过 {skipped_count} 个弹幕数不足的视频")


def start_scheduled_crawling(total=600, interval=60):
    """
    启动定时爬虫
    :param total: 每次要抓取的视频总数
    :param interval: 定时间隔（分钟）
    """
    logger.info(f"启动定时爬虫，每{interval}分钟执行一次，每次抓取{total}个视频")
    
    # 立即执行一次
    crawl_videos(total)
    
    # 安排定时任务
    schedule.every(interval).minutes.do(crawl_videos, total=total)
    
    # 无限循环，执行定时任务
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次


def main():
    """
    主函数，串联整个工作流
    """
    # 默认抓取1000个视频，每30分钟执行一次
    start_scheduled_crawling(total=1000, interval=30)


if __name__ == "__main__":
    main()