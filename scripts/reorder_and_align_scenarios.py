import os, json

root = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

links_path = os.path.join(root, 'all_25_real_workspace_links.json')
with open(links_path, 'r', encoding='utf-8') as f:
    links = json.load(f)

modules_data = [
    {
        "id": "module-1",
        "tag": "核心功能演練一",
        "title": "智慧型畫布 (Smart Canvas) 與團隊任務指派",
        "intro": "在 Google Docs 中輸入 <code>@</code> 符號，即可觸發「智慧型畫布」快捷選單。這能讓文件從單純的文字編輯器，升級為動態的團隊專案管理中心。",
        "scenario": "您正在為校內專案團隊編輯一份「運動會籌備會議紀錄」文件。為了讓團隊學生與教師能清楚知道各自負責的硬體租借（如音響舞台、遮陽帳棚）與秩序冊印製等工作，您需要為不同任務指派具體負責人，並訂定各項任務的完成截止期限。",
        "task_key": "Task 02",
        "file_type": "Google Docs",
        "doc_inst": "請在文件中的「負責人」欄位輸入 @ 插入 @People 人員晶片；在「完成期限」欄位輸入 @ 插入 @Date 日期晶片！",
        "steps": [
            "開啟會議議程 Docs 文件，移至「任務分工表」區段。",
            "在「負責人」欄位輸入 <code>@</code>，選取並插入 <strong><code>@People</code> (人員晶片)</strong>。",
            "在「預計完成日」欄位輸入 <code>@</code>，選取並插入 <strong><code>@Date</code> (日期晶片)</strong>。"
        ]
    },
    {
        "id": "module-2",
        "tag": "核心功能演練二",
        "title": "結構化排版與動態導覽目錄 (Paragraph Styles)",
        "intro": "要讓長篇文件自動生成方便點選跳轉的目錄，必須正確套用「段落樣式 (Paragraph Styles)」（如：標題 1、標題 2），而不是單純手動放大字體。",
        "scenario": "您正在準備一份包含多個章節的「校本課程實施計畫手冊」。文件中包含了課程發展願景、全學期領域配課與多元評量規範。您希望建立一份結構嚴謹的文件，讓開啟檔案者能透過最上方的目錄快速點選跳轉至指定章節。",
        "task_key": "Task 03",
        "file_type": "Google Docs",
        "doc_inst": "請選取文件中的「第一章、第二章、第三章」章節標題套用「標題 1」段落樣式，並在頂部點選「插入 ➔ 頁面元素 ➔ 目錄」！",
        "has_img": True,
        "steps": [
            "選取文件中的章節標題（如「第一章：課程發展願景與核心素養」）。",
            "在工具列將段落樣式切換套用為 <strong><code>標題 1 (Heading 1)</code></strong>。",
            "移至文件開頭，點選選單 <strong>「插入 ➔ 往下拉至最底部 ➔ 目錄 (Table of Contents)」</strong>（或點選「檢視 ➔ 顯示大綱」開啟左側動態大綱）。"
        ]
    },
    {
        "id": "module-3",
        "tag": "核心功能演練三",
        "title": "高效內文檢索與批次修正 (Find and Replace)",
        "intro": "在整理多頁報告或教學素材時，使用快捷鍵 <code>Ctrl + H</code> 可在數秒內完成全篇文件的搜尋與取代。",
        "scenario": "您編輯完一份長達 10 頁的「全校週報」稿件後，才發現自己將本學期新到任的校長姓名全篇都誤打成了舊校長姓名 <code>陳大文</code>。您需要快速定位並將所有錯字一次性更正為新校長姓名 <code>張小明</code>。",
        "task_key": "Task 01",
        "file_type": "Google Docs",
        "doc_inst": "請按下快捷鍵 Ctrl + H 開啟「尋找與取代」，將文件中所有的舊校長姓名「陳大文」，一次性全部取代更正為新校長姓名「張小明」！",
        "steps": [
            "在 Google Docs 中按下快捷鍵 <strong><code>Ctrl + H</code></strong>（或點選選單「編輯 ➔ 尋找與取代」）。",
            "在「尋找」欄位輸入舊校長姓名（例如：<code>陳大文</code>）。",
            "在「替換為」欄位輸入正確的新校長姓名（例如：<code>張小明</code>）。",
            "點選 <strong>「全部替換 (Replace All)」</strong> 一鍵更正全篇。"
        ]
    },
    {
        "id": "module-4",
        "tag": "核心功能演練四",
        "title": "跨語言親師溝通與文件一鍵翻譯 (Translate Document)",
        "intro": "Google Docs 內建機器翻譯引擎，免安裝外掛即可將全篇文件複製並翻譯為全球數十種語言。",
        "scenario": "身為導師，您每週都會編寫「班級每週學習通訊」發送給家長。為了讓班上不同母語背景（如越南語、印尼語、英語）的家長也能無障礙閱讀班級動態與親師座談會通知，您需要快速產出一份完整的雙語翻譯新文件。",
        "task_key": "Task 05",
        "file_type": "Google Docs",
        "doc_inst": "請點選選單「工具 ➔ 翻譯文件」，選擇目標語言（如越南語或印尼語），自動生成一份完整的雙語翻譯新文件！",
        "steps": [
            "開啟中文「班級每週學習通訊」Docs 文件。",
            "點選頂部功能表 <strong>「工具 ➔ 翻譯文件 (Translate Document)」</strong>。",
            "選取目標語言（如越南語或印尼語）並點選「翻譯」，生成雙語翻譯新文件。"
        ]
    },
    {
        "id": "module-5",
        "tag": "核心功能演練五",
        "title": "非同步語音註解與多媒體回饋 (Marketplace Add-ons)",
        "intro": "若希望針對學生的作文或作業給予更具親和力、非同步的「口頭/語音回饋」，可透過 Workspace Marketplace 安裝第三方擴充功能 (如 Mote)。",
        "scenario": "學生在 Google Docs 提交了期末作文〈那一刻，我長大了〉。您希望除了文字批改外，還能透過語音擴充外掛錄製一段親切的口頭說明，給予學生非同步的聽覺建議與鼓勵。",
        "task_key": "Task 04",
        "file_type": "Google Docs",
        "doc_inst": "請點選選單「擴充功能 ➔ 外掛程式 ➔ 取得外掛程式」安裝 Mote 外掛，並在本作文段落新增註解錄製一段語音回饋！",
        "steps": [
            "點選選單 <strong>「擴充功能 ➔ 外掛程式 ➔ 取得外掛程式」</strong>。",
            "在 Marketplace 搜尋並安裝語音回饋外掛 (如 Mote)。",
            "在學生作文段落新增註解，點選「語音錄音」發布聲音回饋。"
        ]
    },
    {
        "id": "module-6",
        "tag": "核心功能演練六",
        "title": "跨軟體行政整合 (行事曆與簡報批註連動)",
        "intro": "Google Docs 能與 Calendar 及 Slides 深度連動，實現一鍵開立會議紀錄與批註指派任務。",
        "scenario": "教研團隊正在進行教學專案討論，開啟了「教研會會議紀錄」文件供所有人共同編輯與腦力激盪，並在討論結束後選取特定段落新增批註 <code>+成員Email</code> 並勾選指派小方塊，精確交付團隊同仁執行。",
        "task_key": "Task 09",
        "file_type": "Google Docs",
        "doc_inst": "請選取文件段落新增註解，輸入 +成員Email 並勾選「指派給...」核取方塊，交付團隊成員執行！",
        "steps": [
            "在 Calendar 活動視窗點選 <strong>「新增會議紀錄 (Add meeting notes)」</strong>。",
            "在 Docs 或簡報內選取段落新增註解，輸入 <strong><code>+成員Email</code></strong>。",
            "<strong>勾選「指派給... (Assign to...)」</strong>核取方塊並點選指派。"
        ]
    }
]

# Build modules HTML
module_cards_html = ""
for idx, m in enumerate(modules_data, 1):
    active_cls = "active" if idx == 1 else ""
    display_style = "display:block;" if idx == 1 else "display:none;"
    
    info = links.get(m["task_key"], {})
    url = info.get("url", "#")
    t_title = info.get("title", m["title"])
    
    img_html = ""
    if m.get("has_img"):
        img_html = '''
        <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:10px; padding:16px; margin:16px 0; text-align:center;">
          <p style="font-size:0.9rem; font-weight:700; color:#1a73e8; margin-bottom:8px;">📷 Google Docs 插入目錄介面對照圖（選單：插入 ➔ 頁面元素 ➔ 目錄）：</p>
          <img src="images/docs_insert_toc_menu.png" alt="Google Docs 插入目錄介面截圖" style="max-width:100%; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.12);">
        </div>
'''

    steps_list = ""
    for s_idx, s in enumerate(m["steps"], 1):
        steps_list += f'''
          <div class="step-item">
            <input type="checkbox" id="m{idx}-s{s_idx}">
            <label for="m{idx}-s{s_idx}">{s}</label>
          </div>'''

    module_cards_html += f'''
      <!-- MODULE {idx} -->
      <div class="module-card {active_cls}" id="module-{idx}" style="{display_style}">
        <span class="tag">{m["tag"]}</span>
        <h2>{m["title"]}</h2>
        <p>{m["intro"]}</p>

        <!-- 1. 黃色區塊：實務教學情境 (置頂放在最上面) -->
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          {m["scenario"]}
        </div>

        <!-- 2. 綠色區塊：線上真實實作檔案與具體修改任務 (緊接在情境下方) -->
        <div style="background:#e6f4ea; border:2px solid #34a853; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#137333; font-size:1.05rem; display:flex; align-items:center; gap:6px;">
              🔗 本單元線上真實 Google Docs 實作檔案：
            </strong>
            <a href="{url}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:10px 22px; border-radius:20px; font-weight:700; font-size:0.92rem; box-shadow:0 3px 8px rgba(0,0,0,0.15); transition:all 0.2s;">📄 點此開啟真實 Google Docs 實作檔</a>
          </div>
          <div style="background:white; border:1px solid #a8dab5; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.88rem; color:#5f6368; margin-bottom:4px;">檔名：<strong>{t_title}</strong></div>
            <div style="font-size:0.95rem; color:#137333; font-weight:700; line-height:1.5;">
              🎯 本檔具體修改任務：<span style="color:#202124; font-weight:500;">{m["doc_inst"]}</span>
            </div>
          </div>
        </div>

        {img_html}

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          {steps_list}
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-{idx}')">📋 複製本單元操作步驟</button>
        </div>
      </div>
'''

full_html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Docs 進階功能與行政自動化研習講義 (互動網頁版)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --primary-light: #e8f0fe;
      --secondary: #34a853;
      --text-main: #202124;
      --text-muted: #5f6368;
      --bg-body: #f8f9fa;
      --bg-card: #ffffff;
      --border: #dadce0;
      --shadow: 0 4px 16px rgba(0,0,0,0.06);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Google Sans', 'Noto Sans TC', sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
    }}

    header {{
      background: var(--primary);
      color: white;
      padding: 24px 32px;
      box-shadow: 0 4px 12px rgba(26,115,232,0.25);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .header-title h1 {{ font-size: 1.5rem; font-weight: 700; }}
    .header-title p {{ font-size: 0.9rem; opacity: 0.9; margin-top: 4px; }}

    .nav-links {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .nav-btn {{
      text-decoration: none;
      background: rgba(255,255,255,0.2);
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{ background: white; color: var(--primary); }}

    .app-layout {{
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
    }}

    @media (max-width: 900px) {{
      .app-layout {{ grid-template-columns: 1fr; }}
    }}

    .sidebar {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      height: fit-content;
      position: sticky;
      top: 100px;
    }}

    .sidebar-heading {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }}

    .menu-item {{
      display: block;
      width: 100%;
      text-align: left;
      border: none;
      background: transparent;
      padding: 12px 14px;
      border-radius: 8px;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      margin-bottom: 6px;
      transition: all 0.2s;
    }}

    .menu-item:hover {{ background: var(--bg-body); color: var(--primary); }}
    .menu-item.active {{ background: var(--primary-light); color: var(--primary); font-weight: 700; }}

    .content-area {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }}

    .module-card {{ display: none; }}
    .module-card.active {{ display: block; animation: fadeIn 0.3s ease-in-out; }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}

    h2 {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 16px; color: var(--primary-dark); }}
    h3 {{ font-size: 1.1rem; font-weight: 700; margin: 20px 0 10px 0; color: var(--text-main); }}
    p {{ margin-bottom: 14px; color: #3c4043; line-height: 1.7; }}

    .scenario-box {{
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
    }}

    .scenario-box strong {{ color: #b06000; }}

    .step-list {{
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin: 20px 0;
    }}

    .step-item {{
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    .step-item input[type="checkbox"] {{
      margin-top: 5px;
      width: 18px;
      height: 18px;
      cursor: pointer;
    }}

    .action-bar {{
      display: flex;
      gap: 12px;
      margin-top: 24px;
    }}

    .btn {{
      border: none;
      padding: 10px 20px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-primary {{ background: var(--primary); color: white; }}
    .btn-primary:hover {{ background: var(--primary-dark); }}

    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #323232;
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 0.9rem;
      display: none;
      z-index: 1000;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>📄 Google Docs 進階功能與行政自動化研習講義</h1>
      <p>實務情境演練 ‧ 隱形考點融合 ‧ 步驟互動清單</p>
    </div>
    <div class="nav-links">
      <a href="study_guide_app.html" class="nav-btn">📖 回研習主講義</a>
      <a href="quiz_app.html" class="nav-btn" target="_blank">📝 25 題雙語刷題 App</a>
      <a href="lab_exercises_app.html" class="nav-btn" target="_blank">🛠️ 15 個 Lab 練習 App</a>
    </div>
  </header>

  <div class="app-layout">
    
    <!-- Sidebar Navigation -->
    <nav class="sidebar">
      <div class="sidebar-heading">實務演練章節選單</div>
      <button class="menu-item active" onclick="showModule(0)">🎯 工具篇總覽與研習目標</button>
      <button class="menu-item" onclick="showModule(1)">⚙️ 演練一：智慧型畫布 (@Smart Canvas)</button>
      <button class="menu-item" onclick="showModule(2)">📚 演練二：段落樣式與自動目錄</button>
      <button class="menu-item" onclick="showModule(3)">🔍 演練三：尋找與取代 (Ctrl+H)</button>
      <button class="menu-item" onclick="showModule(4)">🌐 演練四：多語言通訊翻譯</button>
      <button class="menu-item" onclick="showModule(5)">🎙️ 演練五：非同步語音回饋外掛</button>
      <button class="menu-item" onclick="showModule(6)">📅 演練六：會議紀錄與任務指派</button>
    </nav>

    <!-- Main Content Area -->
    <main class="content-area">

      <!-- MODULE 0: OVERVIEW -->
      <div class="module-card active" id="module-0" style="display:block;">
        <span class="tag">研習簡介與教學策略</span>
        <h2>Google Docs 進階功能應用與行政自動化總覽</h2>
        <p>歡迎來到 **Google Docs (Google 文件)** 工具篇講義！本研習單元專為教師與教育行政人員設計，聚焦於如何靈活運用 Google Docs 的進階功能，提升教學素材製作與班級行政處理效率。</p>

        <div style="background:#e8f0fe; border-radius:12px; padding:20px; margin:20px 0;">
          <h3 style="color:#1a73e8; margin-top:0;">💡 本章六大實務演練目標：</h3>
          <ul style="padding-left:20px; line-height:1.8; color:#3c4043;">
            <li><strong>演練一</strong>：運用智慧型畫布 (Smart Canvas) 指派專案負責人與設定截止日期。</li>
            <li><strong>演練二</strong>：正確套用段落樣式 (Paragraph Styles)，一鍵生成動態導覽目錄。</li>
            <li><strong>演練三</strong>：活用快捷鍵 `Ctrl + H` 批次尋找與取代全篇錯誤錯字與作者姓名。</li>
            <li><strong>演練四</strong>：點選選單「翻譯文件」，生成多語言版本的雙語班級通訊。</li>
            <li><strong>演練五</strong>：透由 Workspace Marketplace 安裝擴充外掛，提供非同步口頭語音回饋。</li>
            <li><strong>演練六</strong>：結合日曆會議紀錄 (Meeting Notes) 與批註 `+Email` 核取方塊指派團隊任務。</li>
          </ul>
        </div>
      </div>

      {module_cards_html}

    </main>
  </div>

  <div class="toast" id="toast">已複製操作步驟至剪貼簿！</div>

  <script>
    function showModule(idx) {{
      document.querySelectorAll('.menu-item').forEach((btn, i) => {{
        btn.classList.toggle('active', i === idx);
      }});
      document.querySelectorAll('.module-card').forEach((card, i) => {{
        card.style.display = (i === idx) ? 'block' : 'none';
        card.classList.toggle('active', i === idx);
      }});
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function copySteps(modId) {{
      const mod = document.getElementById(modId);
      const title = mod.querySelector('h2').innerText;
      const steps = Array.from(mod.querySelectorAll('.step-item label'))
        .map((l, i) => `${{i + 1}}. ${{l.innerText}}`)
        .join('\\n');
      
      const text = `【${{title}}】\\n${{steps}}`;
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.style.display = 'block';
        setTimeout(() => toast.style.display = 'none', 2500);
      }});
    }}
  </script>
</body>
</html>
'''

p_docs = os.path.join(root, 'docs_workshop_app.html')
with open(p_docs, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Successfully updated docs_workshop_app.html with reordered layout and matched scenario text!")
