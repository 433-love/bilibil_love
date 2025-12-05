// 全局变量
let allVideos = [];
let currentRankings = [];
let currentSortType = 'confusion_index'; // 默认按疑惑指数排序
let currentShowCount = 10;
let searchQuery = '';

// 性能优化：使用虚拟列表标记
let isUpdating = false;
let updateTimer = null;

// DOM元素
const totalVideosEl = document.getElementById('total-videos');
const averageConfusionEl = document.getElementById('average-confusion');
const maxQuestionsEl = document.getElementById('max-questions');
const maxConfusionEl = document.getElementById('max-confusion');
const confusionChartEl = document.getElementById('confusion-chart');
const sortTypeEl = document.getElementById('sort-type');
const showCountEl = document.getElementById('show-count');
const searchInputEl = document.getElementById('search-input');
const searchBtnEl = document.getElementById('search-btn');
const rankingsListEl = document.getElementById('rankings-list');

// 初始化图表
let confusionChart;

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', () => {
    // 加载数据
    loadData();
    
    // 绑定事件监听器
    bindEventListeners();
});

// 绑定事件监听器
function bindEventListeners() {
    // 排序方式改变 - 使用防抖优化
    sortTypeEl.addEventListener('change', debounce((e) => {
        currentSortType = e.target.value;
        updateRankings();
    }, 300));
    
    // 显示数量改变 - 使用防抖优化
    showCountEl.addEventListener('change', debounce((e) => {
        currentShowCount = e.target.value === 'all' ? Infinity : parseInt(e.target.value);
        updateRankings();
    }, 300));
    
    // 搜索按钮点击 - 使用防抖优化
    searchBtnEl.addEventListener('click', debounce(() => {
        searchQuery = searchInputEl.value.trim();
        updateRankings();
    }, 300));
    
    // 搜索框回车 - 使用防抖优化
    searchInputEl.addEventListener('input', debounce(() => {
        searchQuery = searchInputEl.value.trim();
        updateRankings();
    }, 300));
    
    // 导航链接点击
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // 移除所有active类
            navLinks.forEach(l => l.classList.remove('active'));
            // 添加当前active类
            e.target.closest('.nav-link').classList.add('active');
        });
    });
}

// 加载数据
async function loadData() {
    try {
        // 显示加载动画
        rankingsListEl.innerHTML = '<div class="loading">正在加载数据...</div>';
        
        // 加载JSON数据
        const response = await fetch('rankings_data.json');
        if (!response.ok) {
            throw new Error('数据加载失败');
        }
        
        const data = await response.json();
        allVideos = data.question_rankings; // 初始化为按问号数量排序
        
        // 更新概览数据
        updateOverview(data);
        
        // 初始化排行榜
        updateRankings();
        
        // 绘制图表
        drawChart(data);
        
    } catch (error) {
        console.error('加载数据时出错:', error);
        rankingsListEl.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-exclamation-triangle"></i>
                <h3>数据加载失败</h3>
                <p>请确保已运行爬虫生成数据文件</p>
            </div>
        `;
    }
}

// 更新概览数据
function updateOverview(data) {
    const totalVideos = data.total_videos;
    const averageConfusion = data.average_confusion;
    
    // 计算最大值
    const maxQuestions = Math.max(...allVideos.map(v => v.question_count));
    const maxConfusion = Math.max(...allVideos.map(v => v.confusion_index));
    
    // 更新DOM
    animateNumber(totalVideosEl, 0, totalVideos, 1000);
    animateNumber(averageConfusionEl, 0, averageConfusion, 1000, true);
    animateNumber(maxQuestionsEl, 0, maxQuestions, 1000);
    animateNumber(maxConfusionEl, 0, maxConfusion, 1000, true);
}

// 数字动画
function animateNumber(element, start, end, duration, isDecimal = false) {
    const startTime = performance.now();
    const range = end - start;
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const current = start + range * progress;
        
        if (isDecimal) {
            element.textContent = current.toFixed(2);
        } else {
            element.textContent = Math.floor(current);
        }
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

// 绘制疑惑指数分布图表 - 优化图表性能
function drawChart(data) {
    // 准备数据 - 只处理前50个视频，减少计算量
    const confusionData = allVideos.slice(0, 50).map(v => v.confusion_index);
    
    // 计算分布区间 - 优化计算逻辑
    const maxValue = Math.max(...confusionData);
    const min = 0;
    const max = Math.ceil(maxValue / 10) * 10;
    const interval = 10;
    const intervals = Math.ceil((max - min) / interval);
    
    const labels = [];
    const counts = new Array(intervals).fill(0);
    
    // 优化计数逻辑
    for (let i = 0; i < intervals; i++) {
        const start = min + i * interval;
        const end = start + interval;
        labels.push(`${start}-${end}`);
    }
    
    for (const value of confusionData) {
        const index = Math.floor((value - min) / interval);
        if (index >= 0 && index < intervals) {
            counts[index]++;
        }
    }
    
    // 销毁现有图表（如果存在）
    if (confusionChart) {
        confusionChart.destroy();
    }
    
    // 创建新图表 - 优化配置，减少动画和交互
    confusionChart = new Chart(confusionChartEl, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: '视频数量',
                data: counts,
                backgroundColor: 'rgba(0, 161, 214, 0.6)',
                borderColor: 'rgba(0, 161, 214, 1)',
                borderWidth: 1,
                borderRadius: 8,
                barThickness: 20
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    display: true
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.parsed.y}`;
                        }
                    },
                    enabled: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: '视频数量'
                    },
                    ticks: {
                        stepSize: 1
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: '疑惑指数区间（%）'
                    }
                }
            },
            animation: {
                duration: 800, // 减少动画时长
                easing: 'easeOutQuart'
            },
            interaction: {
                intersect: false,
                mode: 'index'
            },
            elements: {
                point: {
                    radius: 0 // 禁用点，减少渲染量
                }
            }
        }
    });
}

// 更新排行榜
function updateRankings() {
    // 复制所有视频数据
    let filteredVideos = [...allVideos];
    
    // 搜索过滤
    if (searchQuery) {
        const query = searchQuery.toLowerCase();
        filteredVideos = filteredVideos.filter(video => 
            video.title.toLowerCase().includes(query) ||
            video.bvid.toLowerCase().includes(query)
        );
    }
    
    // 排序
    if (currentSortType === 'question_count') {
        filteredVideos.sort((a, b) => b.question_count - a.question_count);
    } else if (currentSortType === 'confusion_index') {
        filteredVideos.sort((a, b) => b.confusion_index - a.confusion_index);
    }
    
    // 限制数量
    filteredVideos = filteredVideos.slice(0, currentShowCount);
    
    // 更新全局排行榜数据
    currentRankings = filteredVideos;
    
    // 渲染排行榜
    renderRankings();
}

// 渲染排行榜
function renderRankings() {
    // 检查是否正在更新
    if (isUpdating) return;
    isUpdating = true;
    
    // 清空列表
    rankingsListEl.innerHTML = '';
    
    // 检查是否有数据
    if (currentRankings.length === 0) {
        rankingsListEl.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-search"></i>
                <h3>没有找到相关视频</h3>
                <p>请尝试调整搜索条件</p>
            </div>
        `;
        isUpdating = false;
        return;
    }
    
    // 使用文档片段减少DOM操作
    const fragment = document.createDocumentFragment();
    
    // 渲染每个排名项
    currentRankings.forEach((video, index) => {
        const rankingItem = createRankingItem(video, index + 1, index);
        fragment.appendChild(rankingItem);
    });
    
    // 一次性添加所有元素
    rankingsListEl.appendChild(fragment);
    
    // 延迟标记为更新完成，防止频繁更新
    setTimeout(() => {
        isUpdating = false;
    }, 100);
}

// 创建排名项元素
function createRankingItem(video, rank, index) {
    const item = document.createElement('div');
    item.className = 'ranking-item';
    
    // 构建视频信息HTML - 使用真实视频封面
    // 调试信息：记录前3个视频的封面URL
    if (index < 3) {
        console.log(`视频 #${rank} 封面URL:`, video.pic_url);
    }
    
    const html = `
        <div class="rankings-col rank-col">
            <div class="rank">${rank}</div>
        </div>
        <div class="rankings-col info-col">
            <div class="video-info">
                <div class="video-thumbnail-container">
                    <img src="${video.pic_url}" 
                         alt="${video.title}" 
                         class="video-thumbnail loaded" 
                         referrerpolicy="no-referrer"
                         crossorigin="anonymous"
                         onerror="console.error('图片加载失败:', this.src); this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2260%22 viewBox=%220 0 80 60%22%3E%3Crect width=%2280%22 height=%2260%22 fill=%22%23f0f0f0%22/%3E%3Ctext x=%2240%22 y=%2235%22 font-size=%2212%22 text-anchor=%22middle%22 fill=%22%23999%22%3E封面加载失败%3C/text%3E%3C/svg%3E';">
                </div>
                <div class="video-details">
                    <h4 class="video-title">${video.title}</h4>
                    <p class="video-bvid">${video.bvid}</p>
                    <div class="confusion-bar">
                        <div class="confusion-progress" style="width: 0%"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="rankings-col stat-col">
            <div class="stat-value">
                <i class="fas fa-comment-dots"></i>
                ${video.total_danmaku.toLocaleString()}
            </div>
        </div>
        <div class="rankings-col stat-col">
            <div class="stat-value">
                <i class="fas fa-question-circle"></i>
                ${video.question_count.toLocaleString()}
            </div>
        </div>
        <div class="rankings-col stat-col">
            <div class="stat-value">
                <i class="fas fa-percentage"></i>
                ${video.confusion_index.toFixed(2)}%
            </div>
        </div>
    `;
    
    item.innerHTML = html;
    
    // 添加点击事件，跳转到B站视频页面
    item.addEventListener('click', () => {
        window.open(`https://www.bilibili.com/video/${video.bvid}`, '_blank');
    });
    
    // 延迟显示进度条动画
    const currentIndex = index;
    setTimeout(() => {
        const progressBar = item.querySelector('.confusion-progress');
        if (progressBar) {
            setTimeout(() => {
                progressBar.style.width = `${Math.min(video.confusion_index, 100)}%`;
            }, 100 + currentIndex * 50); // 错开动画时间，减少卡顿
        }
    }, currentIndex * 30);
    
    return item;
}

// 平滑滚动到指定元素
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

// 格式化数字，添加千分位分隔符
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// 格式化时间
function formatTime(timestamp) {
    const date = new Date(timestamp * 1000);
    return date.toLocaleString();
}

// 防抖函数
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 节流函数
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// 动态更新页面标题
function updatePageTitle(title) {
    document.title = title;
}

// 添加页面加载动画
window.addEventListener('load', () => {
    // 页面加载完成后移除加载动画
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.display = 'none';
    }
});

// 添加滚动监听，显示回到顶部按钮
window.addEventListener('scroll', throttle(() => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const backToTopBtn = document.getElementById('back-to-top');
    
    if (backToTopBtn) {
        if (scrollTop > 300) {
            backToTopBtn.style.display = 'flex';
        } else {
            backToTopBtn.style.display = 'none';
        }
    }
}, 200));