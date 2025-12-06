# Bilibili 视频疑惑指数排行榜

一个基于 Python 的 Bilibili 视频数据采集与可视化项目，用于分析 B 站热门视频的弹幕内容，统计其中包含问号的数量，并计算“疑惑指数”。

## 功能特性

- 📊 **数据采集**：自动抓取 B 站热门视频数据
- 💬 **弹幕分析**：分析视频弹幕，统计问号数量
- 📈 **疑惑指数**：计算视频的疑惑指数（问号数量/弹幕总数）
- 🎨 **可视化展示**：直观的排行榜网页，支持数据筛选和排序
- ⏰ **定时抓取**：每 30 分钟自动更新数据
- 🔍 **弹幕过滤**：只分析弹幕数大于 200 的视频，提高数据质量
- 🚀 **高效稳定**：优化的请求策略，避免被反爬虫机制限制
- 📱 **响应式设计**：适配不同设备屏幕尺寸

## 技术栈

- **后端语言**：Python 3.9+
- **请求库**：`requests`
- **解析库**：`lxml`（用于解析 XML 弹幕）
- **数据库**：`sqlite3`（本地数据存储）
- **定时任务**：`schedule`
- **前端框架**：原生 HTML/CSS/JavaScript
- **图表库**：`Chart.js`（用于数据可视化）
- **图标库**：`Font Awesome`（用于界面图标）

## 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/bilibili-confusion-index.git
   cd bilibili-confusion-index
   ```

2. **安装依赖**
   ```bash
   pip install requests lxml schedule
   ```

## 使用方法

### 1. 运行数据采集器

```bash
python crawler.py
```

这将启动爬虫，默认抓取 1000 个热门视频，每 30 分钟自动更新一次。

### 2. 导出可视化数据

```bash
python export_data.py
```

这将从数据库中导出数据，生成 `rankings_data.json` 文件，用于前端可视化展示。

### 3. 启动 HTTP 服务器

```bash
python -m http.server 8000
```

### 4. 访问可视化页面

在浏览器中访问：`http://localhost:8000/rankings.html`

## 项目结构

```
bilibili-confusion-index/
├── config.py          # 配置文件，包含 API 地址和数据库配置
├── crawler.py         # 爬虫主程序，包含数据采集和分析逻辑
├── export_data.py     # 数据导出脚本，生成可视化数据
├── rankings.html      # 数据可视化页面
├── styles.css         # 页面样式文件
├── script.js          # 前端交互脚本
├── bilibili_confusion.db  # SQLite 数据库文件（运行后生成）
├── rankings_data.json     # 可视化数据文件（运行 export_data.py 后生成）
└── bilibili_crawler.log   # 爬虫日志文件（运行后生成）
```

## 配置说明

### 修改抓取数量和间隔

在 `crawler.py` 文件中修改以下参数：

```python
def main():
    # 默认抓取 1000 个视频，每 30 分钟执行一次
    start_scheduled_crawling(total=1000, interval=30)
```

### 修改 HTTP 请求头

在 `config.py` 文件中修改 `HEADERS` 配置：

```python
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    # 其他请求头...
}
```

## 运行结果

### 数据概览
- 显示总视频数、平均疑惑指数、最多问号数、最高疑惑指数
- 疑惑指数分布图表

### 排行榜
- 按问号数量排序的排行榜
- 按疑惑指数排序的排行榜
- 支持搜索和筛选
- 显示视频封面、标题、弹幕总数、问号数量、疑惑指数

## 注意事项

### 反爬虫策略
- B 站有严格的反爬虫机制，请勿频繁请求
- 爬虫已内置随机延时和重试机制，提高稳定性
- 建议不要修改默认的请求间隔

### 数据存储
- 数据存储在 `bilibili_confusion.db` SQLite 数据库中
- 定期备份数据库文件，防止数据丢失

### 安全问题
- 请勿将数据库文件直接暴露在公网
- 建议使用 HTTPS 协议，保护数据传输

### 性能优化
- 如果服务器配置较低，建议减少抓取视频数量
- 可以调整定时间隔，减少服务器负载

## 常见问题排查

### 爬虫无法连接到 B 站 API
- 检查网络连接
- 检查请求头配置
- 检查 IP 是否被 B 站限制

### 封面图片无法显示
- 检查 `pic_url` 是否正确（应该是 HTTPS 协议）
- 检查浏览器控制台是否有跨域错误
- 图片加载失败时会自动显示占位图

### 数据库操作错误
- 检查数据库文件权限
- 检查数据库表结构是否正确
- 检查 SQL 语句是否正确

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- 项目地址：https://github.com/yourusername/bilibili-confusion-index](https://github.com/433-love/bilibil_love
- 作者：Love433
- 邮箱：2832490995@qq.com

## 更新日志

### v1.0.0 (2025-12-05)
- 初始版本
- 支持 B 站热门视频抓取
- 弹幕分析和疑惑指数计算
- 数据可视化展示
- 定时抓取功能
- 弹幕数过滤功能

### v1.0.1 (2025-12-05)
- 修复了视频封面显示问题
- 优化了爬虫速率
- 增强了错误处理机制
- 完善了 README 文档

---

感谢使用 Bilibili 视频疑惑指数排行榜！如果您有任何问题或建议，欢迎随时提出。
