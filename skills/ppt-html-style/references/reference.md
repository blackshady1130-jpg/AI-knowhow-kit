# PPT-HTML-Style 完整参考模板

本文件包含完整的CSS定义和每个组件的HTML代码模板。在BUILD阶段按需读取。

---

## 1. HTML骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{报告标题}}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  theme: { extend: { colors: {
    background: '#FFFFFF',
    foreground: '#040404',
    primary: '#0033CC',
    accent: '#FF6A00',
    secondary: '#F5F5F7',
    muted: '#F5F5F7',
    'muted-foreground': '#979AA7',
    border: '#CFD0D7',
    success: '#16a34a',
    warning: '#FF6A00',
    destructive: '#dc2626',
  }}}
}
</script>
<style>
{{完整CSS — 见下方Section 2}}
</style>
</head>
<body>
<div class="deck-viewport">
<div class="deck-container" id="deck">

{{所有slide sections}}

</div>
<!-- 导航按钮 -->
<div class="nav-arrow nav-prev disabled" id="prevBtn" onclick="navigate(-1)">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
</div>
<div class="nav-arrow nav-next" id="nextBtn" onclick="navigate(1)">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
</div>
<div class="page-indicator" id="indicator"></div>
</div>
<div class="keyboard-hint">← → 翻页</div>
<script>
{{翻页JS — 见下方Section 4}}
</script>
</body>
</html>
```

---

## 2. 完整CSS

直接复制到`<style>`标签内：

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;500;700;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: #111827;
  font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow: hidden;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* === 幻灯片容器 === */
.deck-viewport { width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; }
.deck-container { width: min(94vw, 1140px); aspect-ratio: 16 / 9; position: relative; border-radius: 4px; overflow: hidden; box-shadow: 0 30px 100px rgba(0,0,0,.4); }

/* === 单张幻灯片 === */
.slide { position: absolute; inset: 0; background: #FFFFFF; display: none; flex-direction: column; overflow: hidden; }
.slide.active { display: flex; }

/* === 右侧蓝色竖条装饰 === */
.slide::after {
  content: '';
  position: absolute;
  right: 0;
  top: 15%;
  width: 5px;
  height: 35%;
  background: #0033CC;
  border-radius: 3px 0 0 3px;
}

/* === 顶部导航条 === */
.slide-topbar {
  padding: 20px 48px 0 48px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}
.slide-topbar-left {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #979AA7;
  letter-spacing: 0.02em;
}
.slide-topbar-left .part-num { color: #0033CC; font-weight: 500; }
.slide-topbar-right {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #979AA7;
}

/* === 内容区 === */
.slide-body { flex: 1; padding: 24px 48px 20px 48px; display: flex; flex-direction: column; overflow: hidden; }

/* === 几何装饰元素（封面/结束页） === */
.geo-dots {
  position: absolute;
  top: 24px;
  right: 48px;
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 6px;
  opacity: 0.35;
}
.geo-dots span { width: 4px; height: 4px; background: #CFD0D7; border-radius: 1px; display: block; }

/* === 底部信息栏 === */
.slide-bottombar {
  padding: 0 48px 16px 48px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
}
.slide-bottombar-left { font-size: 0.68rem; color: #979AA7; }
.slide-bottombar-right { font-size: 0.7rem; color: #979AA7; font-family: 'JetBrains Mono', monospace; }

/* === 排版 === */
.title-xl { font-size: 2rem; font-weight: 900; color: #040404; line-height: 1.3; }
.title-lg { font-size: 1.5rem; font-weight: 700; color: #040404; line-height: 1.3; }
.title-md { font-size: 1.1rem; font-weight: 700; color: #040404; line-height: 1.4; }
.subtitle { font-size: 0.85rem; color: #979AA7; line-height: 1.5; margin-top: 8px; }
.body-text { font-size: 0.82rem; color: #333; line-height: 1.7; }
.caption { font-size: 0.72rem; color: #979AA7; }
.mono { font-family: 'JetBrains Mono', monospace; }

/* === 蓝色分隔线 === */
.blue-line { height: 2px; background: #0033CC; width: 100%; margin: 16px 0; }
.blue-line-thin { height: 1px; background: #0033CC; opacity: 0.3; width: 100%; }

/* === 模块卡片 === */
.module-card {
  border-top: 2.5px solid #0033CC;
  padding: 16px 18px;
  background: #FAFBFC;
  border-radius: 0 0 6px 6px;
}
.module-card-accent {
  border-top: 2.5px solid #FF6A00;
  padding: 16px 18px;
  background: #FFFBF8;
  border-radius: 0 0 6px 6px;
}
.module-card-grey {
  border-top: 2.5px solid #CFD0D7;
  padding: 16px 18px;
  background: #FAFBFC;
  border-radius: 0 0 6px 6px;
}

/* === 数据表格 === */
.data-table { border-collapse: collapse; width: 100%; font-size: 0.78rem; }
.data-table th {
  background: #0033CC;
  color: white;
  font-weight: 500;
  font-size: 0.72rem;
  padding: 8px 12px;
  text-align: left;
}
.data-table td { padding: 7px 12px; border-bottom: 1px solid #E8E9ED; color: #333; }
.data-table tr:last-child td { border-bottom: none; }
.data-table tr:nth-child(even) { background: #F8F9FA; }

/* === KPI组件 === */
.kpi-block { text-align: center; }
.kpi-value { font-size: 1.6rem; font-weight: 900; line-height: 1.2; font-family: 'JetBrains Mono', monospace; }
.kpi-label { font-size: 0.7rem; color: #979AA7; margin-top: 4px; }
.kpi-note { font-size: 0.62rem; color: #979AA7; margin-top: 2px; }

/* === 进度条 === */
.progress-bar { background: #E8E9ED; border-radius: 4px; height: 8px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 4px; }

/* === 标签 === */
.pill { font-size: 0.68rem; padding: 3px 10px; border-radius: 20px; font-weight: 500; display: inline-block; }
.pill-blue { background: rgba(0,51,204,.08); color: #0033CC; }
.pill-orange { background: rgba(255,106,0,.08); color: #FF6A00; }
.pill-green { background: rgba(22,163,74,.08); color: #16a34a; }
.pill-grey { background: #F0F2F5; color: #666; }

/* === 引用块 === */
.quote-block { padding-left: 12px; border-left: 2px solid #0033CC; }

/* === 提示框/Callout === */
.callout { padding: 12px 16px; border-radius: 6px; font-size: 0.8rem; line-height: 1.6; }
.callout-blue { background: #F0F4FF; border-left: 3px solid #0033CC; }
.callout-orange { background: #FFFBF8; border-left: 3px solid #FF6A00; }
.callout-green { background: #F0FFF4; border-left: 3px solid #16a34a; }

/* === Cover特殊样式 === */
.slide-cover { justify-content: center; align-items: flex-start; padding: 60px 72px; }
.slide-cover::after { top: 20%; height: 40%; }

/* === Divider（目录页等无右侧蓝条） === */
.slide-divider::after { display: none; }

/* === 导航箭头 === */
.nav-arrow { position: absolute; top: 50%; transform: translateY(-50%); width: 38px; height: 38px; border-radius: 50%; background: rgba(255,255,255,.9); border: 1px solid rgba(0,0,0,.06); box-shadow: 0 2px 8px rgba(0,0,0,.1); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all .15s; z-index: 100; color: #040404; }
.nav-arrow:hover { background: #fff; box-shadow: 0 4px 16px rgba(0,0,0,.18); }
.nav-arrow.disabled { opacity: .15; pointer-events: none; }
.nav-prev { left: -52px; }
.nav-next { right: -52px; }

/* === 页面指示器 === */
.page-indicator { position: absolute; bottom: -30px; left: 50%; transform: translateX(-50%); display: flex; gap: 5px; align-items: center; }
.page-dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(255,255,255,.2); transition: all .2s; cursor: pointer; }
.page-dot.active { background: #FF6A00; transform: scale(1.4); }
.page-number { color: rgba(255,255,255,.4); font-size: 11px; margin-left: 10px; font-family: 'JetBrains Mono', monospace; }

.keyboard-hint { position: fixed; bottom: 10px; right: 14px; font-size: 10px; color: rgba(255,255,255,.25); font-family: 'JetBrains Mono', monospace; }
```

---

## 3. 组件HTML模板

### 3.1 封面页

```html
<section class="slide slide-cover active">
  <div class="geo-dots" style="top: 40px; right: 60px;">
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
  </div>
  <div style="margin-top: auto;">
    <div style="font-size: 2.4rem; font-weight: 900; line-height: 1.25; color: #040404;">
      {{主标题第一行}}<br>
      <span style="color: #0033CC;">{{蓝色关键词}}</span>{{标题剩余部分}}
    </div>
    <div style="margin-top: 20px; font-size: 0.9rem; color: #979AA7; line-height: 1.6;">
      {{副标题/一句话描述}}
    </div>
  </div>
  <div style="margin-top: auto; display: flex; align-items: center; gap: 16px;">
    <div style="height: 3px; width: 48px; background: #0033CC; border-radius: 2px;"></div>
    <div style="font-size: 0.78rem; color: #979AA7;">{{团队名}} · {{日期}}</div>
  </div>
</section>
```

### 3.2 目录页

```html
<section class="slide slide-divider">
  <div class="slide-topbar">
    <div class="slide-topbar-left">CONTENTS · 目录</div>
    <div class="slide-topbar-right">02 / {{总页数}}</div>
  </div>
  <div class="slide-body" style="padding-top: 16px;">
    <div class="title-xl" style="margin-bottom: 20px;">目录 · Contents</div>
    <div class="blue-line" style="margin: 0 0 24px 0;"></div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex: 1;">
      <!-- 每个PART一个module-card -->
      <div class="module-card">
        <div class="mono" style="font-size: 0.72rem; color: #0033CC; font-weight: 500;">PART 01</div>
        <div style="font-size: 1.1rem; font-weight: 700; margin-top: 6px;">{{PART名称}}</div>
        <div class="caption" style="margin-top: 6px;">{{关键词 · 关键词 · 关键词}}</div>
        <div class="mono caption" style="margin-top: 10px;">P. 03 - 04</div>
      </div>
      <!-- 重复... -->
    </div>
  </div>
  <div class="slide-bottombar">
    <div></div>
    <div style="font-size: 0.68rem; color: #979AA7;">← → 翻页</div>
  </div>
</section>
```

### 3.3 标准内容页

```html
<section class="slide">
  <div class="slide-topbar">
    <div class="slide-topbar-left"><span class="part-num">PART 01</span> · {{章节名}}</div>
    <div class="slide-topbar-right">{{当前页}} / {{总页数}}</div>
  </div>
  <div class="slide-body">
    <div class="title-lg">{{标题（一句话结论）}}</div>
    <div class="subtitle">{{补充说明}}</div>
    <div class="blue-line"></div>
    <!-- 以下区域放组件组合 -->
    {{内容组件}}
  </div>
  <div class="slide-bottombar">
    <div class="slide-bottombar-left">{{数据来源}}</div>
    <div class="slide-bottombar-right"></div>
  </div>
</section>
```

### 3.4 KPI卡片组

```html
<div style="display: grid; grid-template-columns: repeat({{N}}, 1fr); gap: 10px; margin-bottom: 14px;">
  <div style="text-align: center; padding: 12px 6px; background: #F0F4FF; border-radius: 6px; border-top: 3px solid #0033CC;">
    <div style="font-size: 0.68rem; color: #979AA7;">{{标签}}</div>
    <div class="kpi-value" style="color: #0033CC;">{{数值}}</div>
    <div class="kpi-label">{{说明}}</div>
  </div>
  <!-- 颜色变体：
       蓝色主：background: #F0F4FF; border-top: 3px solid #0033CC; color: #0033CC
       橙色强调：background: #FFFBF8; border-top: 3px solid #FF6A00; color: #FF6A00
       绿色正面：background: #F0FFF4; border-top: 3px solid #16a34a; color: #16a34a
       灰色次要：background: #F8F9FA; border-top: 3px solid #979AA7; color: #666
  -->
</div>
```

### 3.5 数据表格

```html
<table class="data-table">
  <thead>
    <tr>
      <th>{{列名1}}</th>
      <th class="mono">{{列名2}}</th>
      <!-- 数字列加class="mono" -->
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>{{行名}}</strong></td>
      <td class="mono">{{数值}}</td>
      <!-- 高亮最新数据：style="font-weight:700; color:#0033CC;" -->
      <!-- 增速标注：<span class="pill pill-blue">+525%</span> -->
    </tr>
    <!-- 合计行特殊样式 -->
    <tr style="background: #F0F4FF !important;">
      <td><strong>合计</strong></td>
      <td class="mono" style="font-weight:900; color:#0033CC;">{{汇总值}}</td>
    </tr>
  </tbody>
</table>
<div class="caption" style="margin-top: 8px;">{{表格脚注}}</div>
```

### 3.6 进度条组

```html
<div style="display: flex; flex-direction: column; gap: 10px;">
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
      <span class="body-text">{{名称}}</span>
      <span class="mono" style="font-size: 0.78rem; font-weight: 700; color: #0033CC;">{{百分比}}%</span>
    </div>
    <div class="progress-bar">
      <div class="progress-fill" style="width: {{百分比}}%; background: #0033CC;"></div>
    </div>
  </div>
  <!-- 第二条用 #FF6A00，第三条用 #16a34a，第四条用 #979AA7 -->
</div>
```

### 3.7 双栏对比布局

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex: 1;">
  <div class="module-card">
    <div class="title-md">{{左标题}}</div>
    <div class="body-text" style="margin-top: 8px;">{{左内容}}</div>
  </div>
  <div class="module-card-accent">
    <div class="title-md">{{右标题}}</div>
    <div class="body-text" style="margin-top: 8px;">{{右内容}}</div>
  </div>
</div>
```

### 3.8 引用块 + Callout组合

```html
<!-- 引用块：用于原话/核心观点 -->
<div class="quote-block" style="margin: 12px 0;">
  <div class="body-text" style="font-style: italic;">{{引用内容}}</div>
  <div class="caption" style="margin-top: 4px;">— {{来源}}</div>
</div>

<!-- Callout：用于结论/判断/提醒 -->
<div class="callout callout-blue" style="margin: 10px 0;">
  <strong>{{结论标题}}</strong><br>
  <span class="body-text">{{详细说明}}</span>
</div>

<!-- 橙色警告Callout -->
<div class="callout callout-orange" style="margin: 10px 0;">
  <strong>{{警告/重要发现}}</strong><br>
  <span class="body-text">{{说明}}</span>
</div>
```

### 3.9 结论汇总页（多Callout grid）

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; flex: 1;">
  <div class="callout callout-blue">
    <div style="font-weight: 700; font-size: 0.82rem; margin-bottom: 4px;">{{结论1标题}}</div>
    <div class="body-text">{{详细}}</div>
  </div>
  <div class="callout callout-orange">
    <div style="font-weight: 700; font-size: 0.82rem; margin-bottom: 4px;">{{结论2标题}}</div>
    <div class="body-text">{{详细}}</div>
  </div>
  <!-- 可以3-6个callout组成grid -->
</div>
```

### 3.10 结束页

```html
<section class="slide slide-cover">
  <div class="geo-dots" style="top: 40px; right: 60px;">
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
  </div>
  <div style="margin-top: auto;">
    <div style="font-size: 2rem; font-weight: 900; color: #040404;">Thank You</div>
    <div style="margin-top: 16px; font-size: 0.85rem; color: #979AA7; line-height: 1.6;">
      {{结束语或核心结论回顾}}
    </div>
  </div>
  <div style="margin-top: auto; display: flex; align-items: center; gap: 16px;">
    <div style="height: 3px; width: 48px; background: #0033CC; border-radius: 2px;"></div>
    <div style="font-size: 0.78rem; color: #979AA7;">{{来源/团队}}</div>
  </div>
</section>
```

---

## 4. 翻页JavaScript

直接复制到`<script>`标签内：

```javascript
(function() {
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  let current = 0;

  const indicator = document.getElementById('indicator');
  for (let i = 0; i < total; i++) {
    const dot = document.createElement('div');
    dot.className = 'page-dot' + (i === 0 ? ' active' : '');
    dot.onclick = () => goTo(i);
    indicator.appendChild(dot);
  }
  const numEl = document.createElement('span');
  numEl.className = 'page-number';
  numEl.textContent = `1 / ${total}`;
  indicator.appendChild(numEl);

  function goTo(index) {
    if (index < 0 || index >= total) return;
    slides[current].classList.remove('active');
    indicator.children[current].classList.remove('active');
    current = index;
    slides[current].classList.add('active');
    indicator.children[current].classList.add('active');
    numEl.textContent = `${current + 1} / ${total}`;
    document.getElementById('prevBtn').classList.toggle('disabled', current === 0);
    document.getElementById('nextBtn').classList.toggle('disabled', current === total - 1);
  }

  window.navigate = function(dir) { goTo(current + dir); };

  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') navigate(1);
    else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') navigate(-1);
  });
})();
```

---

## 5. 设计细节备忘

### 配色语义
| 颜色 | 用途 |
|------|------|
| #0033CC 蓝 | 结构性元素（表头/蓝条/分隔线/PART标识）+ 主要数据 |
| #FF6A00 橙 | 高亮/强调（竞品/增速/突破/重要发现） |
| #16a34a 绿 | 正面/增长/达标 |
| #979AA7 灰 | 说明性文字/次要信息/caption |
| #CFD0D7 浅灰 | 边框/灰色卡片顶边/geo-dots |

### 字号层级
| 场景 | 字号 | 字重 |
|------|------|------|
| 封面标题 | 2.4rem | 900 |
| title-xl（目录） | 2rem | 900 |
| title-lg（内容页标题） | 1.5rem | 700 |
| title-md（卡片标题） | 1.1rem | 700 |
| KPI数字 | 1.6rem | 900 |
| 副标题 | 0.85rem | 400 |
| 正文 | 0.82rem | 400 |
| 表格 | 0.78rem | 400 |
| 表头 | 0.72rem | 500 |
| caption/pill | 0.68-0.72rem | 500 |

### 间距标准
| 位置 | 值 |
|------|-----|
| slide内边距（左右） | 48px |
| slide内边距（上） | 24px（body区） / 20px（topbar） |
| 组件间距 | 12-16px |
| grid gap | 10-20px（根据内容密度） |
| blue-line margin | 16px 上下 |
| 卡片内padding | 16px 18px |

### 关键注意事项
1. 第一张slide加`active`class，其余不加
2. 封面页第一个`<section>`必须含`active`
3. 页码格式严格为`"03 / 09"`（两位数，中间空格/空格）
4. 右侧蓝条通过`::after`伪元素实现，无需手动添加HTML
5. 封面和结束页的`slide-cover`已内置无topbar/bottombar的布局
6. 目录页用`slide-divider`禁用右侧蓝条
7. 所有数字/百分比/代码用`.mono`标记，确保JetBrains Mono渲染
8. 表格合计行用`style="background: #F0F4FF !important;"`覆盖条纹色
