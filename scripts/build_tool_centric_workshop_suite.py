import json, os, re

links_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\all_25_real_workspace_links.json'
with open(links_path, 'r', encoding='utf-8') as f:
    links = json.load(f)

path_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_app, 'r', encoding='utf-8') as f:
    html = f.read()

tool_bar_html = '''
    <!-- 10 大工具快捷分類頁籤 -->
    <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:20px; padding:12px; background:white; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.05);" id="toolFilterBar">
      <button class="tool-filter-btn active" onclick="filterByTool('all', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#1a73e8; color:white;">🌟 全部 25 個演練</button>
      <button class="tool-filter-btn" onclick="filterByTool('docs', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#e8f0fe; color:#1a73e8;">📄 1. Google Docs (6項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('calendar', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#e8f0fe; color:#1a73e8;">📅 2. Google Calendar (3項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('classroom', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#e6f4ea; color:#137333;">🏫 3. Google Classroom (3項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('slides', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#fef7e0; color:#b06000;">🎨 4. Google Slides (3項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('sites', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#f3e8fd; color:#7b1fa2;">🌐 5. Google Sites (2項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('sheets', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#e6f4ea; color:#137333;">📊 6. Google Sheets (2項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('meet', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#e0f2f1; color:#00695c;">📹 7. Google Meet (2項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('practicesets', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#fef3c7; color:#d97706;">📝 8. Practice Sets (2項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('forms', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#ede7f6; color:#512da8;">📝 9. Google Forms (1項)</button>
      <button class="tool-filter-btn" onclick="filterByTool('gmail', this)" style="border:none; padding:8px 14px; border-radius:16px; font-weight:700; font-size:0.85rem; cursor:pointer; background:#fce8e6; color:#c5221f;">✉️ 10. Gmail與行政 (2項)</button>
    </div>
'''

filter_js = '''
  <script>
    let currentToolFilter = 'all';

    function filterByTool(toolCategory, btnEl) {
      currentToolFilter = toolCategory;
      document.querySelectorAll('.tool-filter-btn').forEach(b => {
        b.style.background = '#e8f0fe';
        b.style.color = '#1a73e8';
        b.classList.remove('active');
      });
      btnEl.style.background = '#1a73e8';
      btnEl.style.color = 'white';
      btnEl.classList.add('active');
      filterTasks();
    }

    function filterTasks() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.task-card');
      
      cards.forEach(card => {
        const kw = card.getAttribute('data-keywords').toLowerCase();
        const text = card.innerText.toLowerCase();
        
        const matchesQuery = !q || kw.includes(q) || text.includes(q);
        let matchesTool = true;

        if (currentToolFilter === 'docs') matchesTool = kw.includes('docs');
        else if (currentToolFilter === 'calendar') matchesTool = kw.includes('calendar');
        else if (currentToolFilter === 'classroom') matchesTool = kw.includes('classroom');
        else if (currentToolFilter === 'slides') matchesTool = kw.includes('slides');
        else if (currentToolFilter === 'sites') matchesTool = kw.includes('sites');
        else if (currentToolFilter === 'sheets') matchesTool = kw.includes('sheets');
        else if (currentToolFilter === 'meet') matchesTool = kw.includes('meet');
        else if (currentToolFilter === 'practicesets') matchesTool = kw.includes('practice');
        else if (currentToolFilter === 'forms') matchesTool = kw.includes('forms');
        else if (currentToolFilter === 'gmail') matchesTool = kw.includes('gmail') || kw.includes('外掛') || kw.includes('代理');

        if (matchesQuery && matchesTool) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
'''

if 'toolFilterBar' not in html:
    html = html.replace('<div id="taskList">', tool_bar_html + '<div id="taskList">')
    html = re.sub(r'<script>.*?</script>', filter_js, html, flags=re.DOTALL)
    with open(path_app, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added 10 Tool Filter Bar to hands_on_tasks_app.html!")
