# Bilibili视频数据采集器实现计划

## 1. 数据库设计
- 创建SQLite数据库 `bilibili_confusion.db`
- 创建表 `video_stats`，包含字段：bvid, aid, cid, title, pic_url, total_danmaku, question_count, confusion_index, created_at

## 2. 代码结构设计

### config.py
- 存放Headers配置（模拟Chrome浏览器）
- 数据库连接函数
- 其他常量配置

### crawler.py
- 导入必要的库（requests, lxml, sqlite3, logging, time, random）
- 实现获取热门视频列表的函数
- 实现获取视频详情的函数
- 实现获取和分析弹幕的函数
- 实现数据存储的函数
- 实现排行榜生成函数
- 主函数，串联整个工作流

## 3. 爬虫工作流实现
- Step 1: 获取热门视频列表（Top 50）
- Step 2: 遍历视频列表，获取每个视频的详细信息
- Step 3: 获取每个视频的弹幕内容，分析包含问号的数量
- Step 4: 计算疑惑指数，将数据存入数据库
- Step 5: 从数据库查询数据，生成排行榜

## 4. 排行榜功能实现
- 从数据库中查询所有视频数据
- 支持按照 `question_count`（问号数量）或 `confusion_index`（疑惑指数）排序
- 展示Top N视频（默认Top 10）
- 在命令行中清晰展示排行榜信息
- 包含视频标题、问号数量、疑惑指数等关键信息

## 5. 非功能性需求实现
- Headers伪装：每个请求带上User-Agent
- 随机延时：1.0到3.0秒的随机等待
- 异常处理：网络请求失败、XML解析失败等情况的处理

## 6. API使用
- 热门视频列表：`https://api.bilibili.com/x/web-interface/popular`
- 视频详情：`https://api.bilibili.com/x/web-interface/view`
- 弹幕内容：`https://comment.bilibili.com/{cid}.xml`