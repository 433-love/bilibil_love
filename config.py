import sqlite3

# 数据库配置
DB_NAME = 'bilibili_confusion.db'

# Headers配置，模拟Chrome浏览器
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}

# API配置
POPULAR_VIDEO_URL = 'https://api.bilibili.com/x/web-interface/popular'
VIDEO_DETAIL_URL = 'https://api.bilibili.com/x/web-interface/view'
DANMAKU_URL = 'https://comment.bilibili.com/{cid}.xml'


def get_db_connection():
    """
    获取数据库连接
    :return: SQLite连接对象
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """
    初始化数据库，创建表
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 创建video_stats表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS video_stats (
            bvid TEXT PRIMARY KEY,
            aid INTEGER,
            cid INTEGER,
            title TEXT,
            pic_url TEXT,
            total_danmaku INTEGER,
            question_count INTEGER,
            confusion_index REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()