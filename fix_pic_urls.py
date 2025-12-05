"""
修复数据库中的图片URL，将http://改为https://
"""
import sqlite3
from config import get_db_connection

def fix_pic_urls():
    """将数据库中所有http://开头的pic_url改为https://"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 统计需要修复的记录数
    cursor.execute("SELECT COUNT(*) FROM video_stats WHERE pic_url LIKE 'http://%'")
    count_before = cursor.fetchone()[0]
    print(f"发现 {count_before} 条需要修复的记录")
    
    if count_before > 0:
        # 更新所有http://开头的URL为https://
        cursor.execute("""
            UPDATE video_stats 
            SET pic_url = REPLACE(pic_url, 'http://', 'https://') 
            WHERE pic_url LIKE 'http://%'
        """)
        conn.commit()
        
        # 验证修复结果
        cursor.execute("SELECT COUNT(*) FROM video_stats WHERE pic_url LIKE 'http://%'")
        count_after = cursor.fetchone()[0]
        
        print(f"修复完成！修复了 {count_before - count_after} 条记录")
        print(f"剩余 {count_after} 条http://记录（如果为0则全部修复成功）")
        
        # 显示几条示例
        cursor.execute("SELECT bvid, title, pic_url FROM video_stats LIMIT 3")
        print("\n示例记录：")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[2]}")
    else:
        print("所有记录的URL都已经是HTTPS，无需修复")
    
    conn.close()

if __name__ == '__main__':
    fix_pic_urls()
