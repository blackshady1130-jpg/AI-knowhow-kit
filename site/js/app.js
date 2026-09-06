/* ============================================================
   AI 行业扫描 NOTES · app.js
   路由 / 渲染 / 证据浏览器 / 引用下钻 / 目录 / 数据可视化
   ============================================================ */

let D = null;
let curTopic = null;
let curNoteView = 'cited';
let curQuery = '';
let curType = '';
let visibleNoteCount = 12;
let activeReference = null;
let hideReferenceTimer = null;
let tocObserver = null;
const TOPIC_ALIASES = { 'AI 影响与安全': 'AI 安全与影响' };

/* ---------- 启动 ---------- */
async function init() {
  const response = await fetch('data.json', { cache: 'no-store' });
  if (!response.ok) throw new Error('Unable to load data.json: ' + response.status);
  D = await response.json();
  window.addEventListener('hashchange', route);
  window.addEventListener('resize', closeReference);
  window.addEventListener('scroll', updateProgress, { passive: true });
  $('footerUpdated').textContent = 'Notes 更新于 ' + D.meta.generated_at;
  route();
}

/* ---------- 路由 ---------- */
function route() {
  closeReference();
  const hash = decodeURIComponent(location.hash || '#home');
  if (hash.startsWith('#topic/')) {
    const name = hash.replace('#topic/', '');
    const resolved = TOPIC_ALIASES[name] || name;
    if (D.topics.some(t => t.name === resolved)) { showTopic(resolved); return; }
  }
  showHome();
}

function showHome() {
  curTopic = null;
  $('homeView').classList.remove('hidden');
  $('topicView').classList.add('hidden');
  navUpdate(null);
  renderHome();
  updateProgress();
  if (location.hash === '#home' || !location.hash) scrollTo(0, 0);
}

function scrollHomeTo(id) {
  if (curTopic) showHome();
  requestAnimationFrame(() =>
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}
function goHomeTo(id) { showHome(); scrollHomeTo(id); }

/* ---------- 首页 ---------- */
function renderHome() {
  const meta = D.meta;
  const whyWan = (meta.total_why_chars / 10000).toFixed(1);
  $('heroStats').innerHTML =
    '<span><b>' + meta.total_notes + '</b>条公开笔记</span>' +
    '<span><b>' + meta.total_topics + '</b>篇主题文章</span>' +
    '<span><b>' + whyWan + '</b>万字原始评论</span>' +
    '<span class="dot">' + esc(rangeText(meta.date_range)) + '</span>';
  $('chapterMeta').textContent = meta.total_notes + ' 条笔记 · ' + rangeText(meta.date_range);

  renderActivity();

  const maxCount = Math.max(...D.topics.map(t => t.count));
  $('topicGrid').innerHTML = D.topics.map(t => {
    const pct = Math.max(6, Math.round(t.count / maxCount * 100));
    return '<a class="dossier-row" href="#topic/' + encodeURIComponent(t.name) + '">' +
      '<div class="dos-chapter">' + esc(t.chapter) + '</div>' +
      '<div>' +
        '<h3 class="dos-name">' + esc(t.name) + '</h3>' +
        '<p class="dos-article">' + esc(t.article_title || t.name) + '</p>' +
        '<p class="dos-desc">' + esc(t.description || t.thesis) + '</p>' +
      '</div>' +
      '<div class="dos-side">' +
        '<span class="dos-count"><b>' + t.count + '</b> 条笔记</span>' +
        '<span class="dos-bar"><i style="width:' + pct + '%"></i></span>' +
        '<span class="dos-arrow">进入文章 →</span>' +
      '</div>' +
    '</a>';
  }).join('');

  const latest = D.notes.slice()
    .sort((a, b) => ((b.date || '') + String(b.id).padStart(4, '0'))
      .localeCompare((a.date || '') + String(a.id).padStart(4, '0')))
    .slice(0, 4);
  $('latestNotes').innerHTML = latest.map(n =>
    '<a class="lat-row" href="#topic/' + encodeURIComponent(n.topics[0]) + '">' +
      '<div class="lat-meta mono"><span><span class="id">#' + n.id + '</span> · ' + esc(typeLabel(n.type)) + '</span><span>' + fmtDate(n.date) + '</span></div>' +
      '<h3 class="lat-title">' + esc(n.title) + '</h3>' +
      '<p class="lat-sum">' + esc(n.why_short || keywordsText(n)) + '</p>' +
      '<span class="lat-topic mono">进入 ' + esc(n.topics[0]) + ' →</span>' +
    '</a>').join('');

  observeReveals();
}

/* 月度收录活动图：运行时从 data.json 统计，不内置数据 */
function renderActivity() {
  const counts = new Map();
  D.notes.forEach(n => {
    const m = /^\d{4}-\d{2}/.exec(n.date || '');
    if (m) counts.set(m[0], (counts.get(m[0]) || 0) + 1);
  });
  if (!counts.size) return;
  const months = [...counts.keys()].sort();
  const seq = [];
  let [y, m] = months[0].split('-').map(Number);
  const [ey, em] = months[months.length - 1].split('-').map(Number);
  while (y < ey || (y === ey && m <= em)) {
    const key = y + '-' + String(m).padStart(2, '0');
    seq.push(key);
    m++; if (m > 12) { m = 1; y++; }
  }
  const max = Math.max(...seq.map(k => counts.get(k) || 0));
  const latestMonth = months[months.length - 1];
  $('activityChart').innerHTML = seq.map(k => {
    const c = counts.get(k) || 0;
    const h = Math.max(3, Math.round(c / max * 100));
    const latest = k === latestMonth ? ' latest' : '';
    return '<div class="act-col' + latest + '">' +
      '<span class="act-tip">' + k.replace('-', '.') + ' · ' + c + ' 条</span>' +
      '<div class="act-bar" style="height:' + h + '%"></div>' +
    '</div>';
  }).join('');
  $('activityRange').textContent =
    months[0].replace('-', '.') + ' — ' + months[months.length - 1].replace('-', '.') +
    ' · ' + seq.length + ' 个月';
}

/* ---------- 主题页 ---------- */
function showTopic(name) {
  curTopic = name;
  const topic = currentTopic();
  if (!topic) return;
  $('homeView').classList.add('hidden');
  $('topicView').classList.remove('hidden');
  navUpdate(topic);
  scrollTo(0, 0);

  $('tvGhost').textContent = topic.chapter;
  $('tvRole').textContent = '主题 ' + topic.chapter + ' · ' + topic.name + ' · ' + (topic.role || '');
  $('tvTitle').textContent = topic.article_title || topic.name;
  $('tvQuestion').textContent = topic.question;
  $('tvThesis').textContent = topic.thesis;
  $('tvMeta').textContent = topic.count + ' 条相关 NOTES · ' + rangeText(topic.date_range || D.meta.date_range) + ' · 文章复核 ' + topic.review_updated_at + ' · Notes 同步 ' + D.meta.generated_at;
  $('reviewSub').textContent = '正文引用 ' + topic.review_note_ids.length + ' 条证据';

  let markdown = topic.review;
  // The page already shows the title and date; keep any prose before the first section.
  markdown = markdown
    .replace(/^\uFEFF?#[ \t]+[^\r\n]*(?:\r?\n|$)/, '')
    .replace(/^\s*\*\*讨论[^\r\n]*\*\*[ \t]*(?:\r?\n|$)/, '')
    .replace(/^\s*---[ \t]*(?:\r?\n|$)/, '')
    .trimStart();
  $('reviewContent').innerHTML = linkRefs(mdParse(markdown));

  buildToc();

  curNoteView = 'cited'; curQuery = ''; curType = ''; visibleNoteCount = 12;
  $('noteSearch').value = ''; $('noteType').value = '';
  renderNoteBrowser();
  setupReferenceControls();
  observeReveals();
  updateProgress();
}

function currentTopic() { return D.topics.find(t => t.name === curTopic); }
function topicNotes(name) { return D.notes.filter(n => n.topics.includes(name)); }

/* ---------- 目录（右侧粘性轨） ---------- */
function buildToc() {
  if (tocObserver) { tocObserver.disconnect(); tocObserver = null; }
  const heads = [...$('reviewContent').querySelectorAll('h2')];
  const toc = $('railToc');
  if (!heads.length) { toc.innerHTML = ''; return; }
  heads.forEach((h, i) => { h.id = 'sec-' + i; });
  toc.innerHTML = heads.map((h, i) =>
    '<a class="toc-link" href="javascript:void 0" data-target="sec-' + i + '">' + esc(h.textContent) + '</a>'
  ).join('');
  toc.querySelectorAll('.toc-link').forEach(a =>
    a.addEventListener('click', () =>
      document.getElementById(a.dataset.target)?.scrollIntoView({ behavior: 'smooth', block: 'start' })));

  tocObserver = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        toc.querySelectorAll('.toc-link').forEach(l => l.classList.remove('active'));
        toc.querySelector('[data-target="' + en.target.id + '"]')?.classList.add('active');
      }
    });
  }, { rootMargin: '-15% 0px -70% 0px' });
  heads.forEach(h => tocObserver.observe(h));
}

/* ---------- 阅读进度尺 ---------- */
function updateProgress() {
  const bar = $('readProgress');
  if (curTopic === null) { bar.style.width = '0'; return; }
  const max = document.documentElement.scrollHeight - innerHeight;
  bar.style.width = (max > 0 ? Math.min(100, scrollY / max * 100) : 0) + '%';
}

/* ---------- 证据浏览器 ---------- */
function setNoteView(view) {
  curNoteView = view;
  visibleNoteCount = 12;
  renderNoteBrowser();
}

function updateNoteFilters() {
  curQuery = $('noteSearch').value.trim().toLowerCase();
  curType = $('noteType').value;
  visibleNoteCount = 12;
  renderNoteBrowser();
}

function noteViewItems() {
  const topic = currentTopic();
  let notes = [];
  if (curNoteView === 'cited') {
    const byId = new Map(D.notes.map(n => [n.id, n]));
    notes = topic.review_note_ids.map(id => byId.get(id)).filter(Boolean);
  } else {
    notes = topicNotes(curTopic).slice()
      .sort((a, b) => ((b.date || '') + String(b.id).padStart(4, '0'))
        .localeCompare((a.date || '') + String(a.id).padStart(4, '0')));
    if (curNoteView === 'recent') notes = notes.slice(0, 18);
  }
  if (curType) notes = notes.filter(n => n.type === curType);
  if (curQuery) notes = notes.filter(n =>
    [n.title, n.why, (n.keywords || []).join(' ')].join(' ').toLowerCase().includes(curQuery));
  return notes;
}

function renderNoteBrowser() {
  document.querySelectorAll('.seg-btn').forEach(b =>
    b.setAttribute('aria-pressed', String(b.dataset.noteView === curNoteView)));
  const notes = noteViewItems();
  const visible = notes.slice(0, visibleNoteCount);
  renderCards(visible);
  const labels = { cited: '文章引用', recent: '最近更新', all: '全部 NOTES' };
  $('notesStatus').textContent = labels[curNoteView] + ' · 显示 ' + visible.length + ' / ' + notes.length + ' 条';
  $('emptyNotes').classList.toggle('hidden', notes.length !== 0);
  $('loadMoreWrap').classList.toggle('hidden', visible.length >= notes.length || notes.length === 0);
}

function loadMoreNotes() {
  visibleNoteCount += 12;
  renderNoteBrowser();
}

function renderCards(notes) {
  const citedIds = new Set(currentTopic()?.review_note_ids || []);
  $('noteList').innerHTML = notes.map(n => {
    const full = esc(n.why || '');
    const more = (n.why || '').length > 220;
    const own = !!n.why;
    const summary = n.why_short || keywordsText(n);
    return '<article class="note-item">' +
      '<div class="nt-head">' +
        '<span class="nid">#' + String(n.id).padStart(3, '0') + '</span>' +
        '<span>' + esc(typeLabel(n.type)) + '</span>' +
        '<span>' + fmtDate(n.date) + '</span>' +
        (citedIds.has(n.id) ? '<span class="nt-flag">正文引用</span>' : '') +
      '</div>' +
      '<h3 class="nt-title">' +
        (n.source_url
          ? '<a href="' + n.source_url + '" target="_blank" rel="noopener">' + esc(n.title) + ' ↗</a>'
          : esc(n.title)) +
      '</h3>' +
      '<p class="nt-judge-label' + (own ? ' own' : '') + '">' +
        (own ? '我的评论' : '索引关键词（原条目无评论）') +
      '</p>' +
      '<p class="nt-summary">' + esc(summary) + '</p>' +
      (more
        ? '<button type="button" class="nt-toggle" onclick="toggleWhy(this)">展开完整评论 ↓</button>' +
          '<div class="nt-full hidden">' + full + '</div>'
        : '') +
      '<p class="nt-kw">' + esc(keywordsText(n)) + '</p>' +
    '</article>';
  }).join('');
}

function toggleWhy(btn) {
  const full = btn.nextElementSibling;
  const opening = full.classList.contains('hidden');
  full.classList.toggle('hidden', !opening);
  btn.textContent = opening ? '收起完整评论 ↑' : '展开完整评论 ↓';
}

/* ---------- 导航 ---------- */
function navUpdate(topic) {
  if (!topic) {
    $('navBC').innerHTML = '<a href="#home" class="nav-brand">AI 行业扫描 Notes</a>';
    $('navMeta').textContent = D.meta.total_notes + ' 条笔记 · ' + rangeText(D.meta.date_range);
  } else {
    $('navBC').innerHTML =
      '<a href="#home">AI 行业扫描 Notes</a><span class="sep">/</span>' +
      '<span class="cur">' + esc(topic.name) + '</span>';
    $('navMeta').textContent = '主题 ' + topic.chapter + ' · ' + topic.count + ' 条笔记';
  }
  $('navChapters').classList.toggle('hidden', !!topic);
}

/* ---------- 引用下钻卡 ---------- */
function linkRefs(html) {
  return html.replace(/#(\d+)/g, (match, id) =>
    D.notes.some(n => n.id === parseInt(id))
      ? '<button type="button" class="note-ref" data-nid="' + id + '" aria-label="查看证据 #' + id + '" aria-expanded="false">' + match + '</button>'
      : match);
}

function setupReferenceControls() {
  document.querySelectorAll('.note-ref').forEach(btn => {
    btn.addEventListener('mouseenter', () => showReference(btn));
    btn.addEventListener('mouseleave', scheduleReferenceClose);
    btn.addEventListener('focus', () => showReference(btn));
    btn.addEventListener('blur', scheduleReferenceClose);
    btn.addEventListener('click', e => {
      e.stopPropagation();
      showReference(btn);
    });
  });
  $('refTip').onmouseenter = () => clearTimeout(hideReferenceTimer);
  $('refTip').onmouseleave = scheduleReferenceClose;
}

function showReference(btn) {
  clearTimeout(hideReferenceTimer);
  if (activeReference && activeReference !== btn) activeReference.setAttribute('aria-expanded', 'false');
  activeReference = btn;
  btn.setAttribute('aria-expanded', 'true');
  const note = D.notes.find(n => n.id === parseInt(btn.dataset.nid));
  if (!note) return;
  const preview = (note.why || keywordsText(note)).substring(0, 220) + ((note.why || '').length > 220 ? '…' : '');
  $('refTip').innerHTML =
    '<div class="tt-title">' + esc(note.title) + '</div>' +
    '<div class="tt-meta">#' + note.id + ' · ' + fmtDate(note.date) + ' · ' + esc(typeLabel(note.type)) + '</div>' +
    '<div class="tt-why">' + esc(preview) + '</div>' +
    (note.source_url ? '<a href="' + note.source_url + '" target="_blank" rel="noopener" class="tt-link">查看原文 ↗</a>' : '');
  positionReference(btn);
  $('refTip').classList.remove('hidden');
}

function positionReference(btn) {
  if (innerWidth <= 640) return;
  const rect = btn.getBoundingClientRect();
  let top = rect.bottom + 10;
  let left = rect.left;
  if (left + 380 > innerWidth - 12) left = innerWidth - 392;
  if (left < 12) left = 12;
  if (top + 340 > innerHeight) top = Math.max(12, rect.top - 349);
  $('refTip').style.top = top + 'px';
  $('refTip').style.left = left + 'px';
}

function scheduleReferenceClose() {
  clearTimeout(hideReferenceTimer);
  hideReferenceTimer = setTimeout(closeReference, 180);
}

function closeReference() {
  clearTimeout(hideReferenceTimer);
  $('refTip')?.classList.add('hidden');
  if (activeReference) activeReference.setAttribute('aria-expanded', 'false');
  activeReference = null;
}

/* ---------- 入场动效 ---------- */
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(en => {
    if (en.isIntersecting) { en.target.classList.add('in'); revealObserver.unobserve(en.target); }
  });
}, { threshold: 0.08 });

function observeReveals() {
  document.querySelectorAll('.reveal:not(.in)').forEach(el => revealObserver.observe(el));
}

/* ---------- 工具 ---------- */
function typeLabel(t) {
  return { 'solid paper': 'Solid paper', '行业动态/评价': '行业动态 / 评价', '观点/文章': '观点 / 文章' }[t] || '资料';
}
function keywordsText(n) { return (n.keywords || []).slice(0, 5).join(' · '); }
function fmtDate(v) { return v ? (v.length >= 7 ? v.substring(0, 7).replace('-', '.') : v) : ''; }
function rangeText(v) { return (v || '').replace(' ~ ', ' – '); }
function $(id) { return document.getElementById(id); }
function esc(v) {
  if (v === null || v === undefined) return '';
  const div = document.createElement('div');
  div.textContent = String(v);
  return div.innerHTML.replace(/\n/g, '<br>');
}

/* marked CDN 失败时的离线降级解析器（覆盖文章用到的基础语法） */
function mdParse(md) {
  if (window.marked && window.marked.parse) return marked.parse(md);
  const escRaw = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const inline = s => escRaw(s)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  const lines = md.split('\n');
  let html = '', list = null, quote = null, para = [];
  const flushPara = () => { if (para.length) { html += '<p>' + para.map(inline).join('<br>') + '</p>'; para = []; } };
  const flushList = () => { if (list) { html += '<' + list + '>' + listItems + '</' + list + '>'; list = null; listItems = ''; } };
  const flushQuote = () => { if (quote) { html += '<blockquote>' + quote + '</blockquote>'; quote = null; } };
  let listItems = '';
  for (const raw of lines) {
    const line = raw.trimEnd();
    if (/^-{3,}$/.test(line.trim())) { flushPara(); flushList(); flushQuote(); html += '<hr>'; continue; }
    const h = /^(#{1,4})\s+(.*)$/.exec(line);
    if (h) { flushPara(); flushList(); flushQuote(); const lv = Math.min(3, Math.max(2, h[1].length)); html += '<h' + lv + '>' + inline(h[2]) + '</h' + lv + '>'; continue; }
    if (/^>\s?/.test(line)) { flushPara(); flushList(); quote = (quote || '') + '<p>' + inline(line.replace(/^>\s?/, '')) + '</p>'; continue; }
    const li = /^[-*]\s+(.*)$/.exec(line);
    if (li) { flushPara(); flushQuote(); if (list !== 'ul') { flushList(); list = 'ul'; } listItems += '<li>' + inline(li[1]) + '</li>'; continue; }
    const oli = /^\d+[.、]\s+(.*)$/.exec(line);
    if (oli) { flushPara(); flushQuote(); if (list !== 'ol') { flushList(); list = 'ol'; } listItems += '<li>' + inline(oli[1]) + '</li>'; continue; }
    if (line.trim() === '') { flushPara(); flushList(); flushQuote(); continue; }
    flushList(); flushQuote();
    para.push(line);
  }
  flushPara(); flushList(); flushQuote();
  return html;
}

/* ---------- 全局事件 ---------- */
document.addEventListener('click', e => {
  if (!$('refTip')?.contains(e.target)) closeReference();
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeReference();
  if (e.key === '/' && curTopic && document.activeElement !== $('noteSearch')) {
    e.preventDefault();
    $('noteSearch')?.focus();
  }
});

init().catch(err => {
  console.error(err);
  document.body.innerHTML =
    '<main style="max-width:640px;margin:0 auto;padding:120px 24px">' +
    '<h1 style="font-family:serif">页面数据加载失败</h1>' +
    '<p>请确认通过本地服务器访问（npm run dev），并刷新重试。</p></main>';
});
