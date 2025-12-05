import sqlite3
import json
from config import get_db_connection

def export_rankings_data():
    """
    从数据库导出排行榜数据为JSON格式
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 获取所有视频数据
    cursor.execute('''
        SELECT bvid, title, pic_url, total_danmaku, question_count, confusion_index
        FROM video_stats
    ''')
    
    videos = cursor.fetchall()
    conn.close()
    
    # 转换为字典列表
    video_list = []
    for video in videos:
        video_list.append({
            'bvid': video['bvid'],
            'title': video['title'],
            'pic_url': video['pic_url'],
            'total_danmaku': video['total_danmaku'],
            'question_count': video['question_count'],
            'confusion_index': video['confusion_index']
        })
    
    # 按问号数量排序
    question_rankings = sorted(video_list, key=lambda x: x['question_count'], reverse=True)
    
    # 按疑惑指数排序
    confusion_rankings = sorted(video_list, key=lambda x: x['confusion_index'], reverse=True)
    
    # 统计信息
    total_videos = len(video_list)
    average_confusion = sum(video['confusion_index'] for video in video_list) / total_videos if total_videos > 0 else 0
    
    # 构建最终数据结构
    data = {
        'total_videos': total_videos,
        'average_confusion': round(average_confusion, 2),
        'question_rankings': question_rankings,
        'confusion_rankings': confusion_rankings
    }
    
    # 写入JSON文件
    with open('rankings_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"成功导出{total_videos}个视频数据到rankings_data.json")


if __name__ == "__main__":
    export_rankings_data()