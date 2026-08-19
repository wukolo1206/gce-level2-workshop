import os

root = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

def build_app(file_name, tool_name, icon, bg_color, border_color, modules):
    menu_items = ""
    module_cards = ""
    
    for idx, m in enumerate(modules):
        active_class = "active" if idx == 0 else ""
        display_style = "display:block;" if idx == 0 else "display:none;"
        
        menu_items += f'<button class="menu-item {active_class}" onclick="showModule({idx})">{m["icon"]} {m["nav_title"]}</button>\n'
        
        steps_html = ""
        for s_idx, s in enumerate(m["steps"], 1):
            steps_html += f'''
          <div class="step-item">
            <input type="checkbox" id="m{idx}-s{s_idx}">
            <label for="m{idx}-s{s_idx}">{s}</label>
          </div>'''
            
        module_cards += f'''
      <!-- MODULE {idx} -->
      <div class="module-card {active_class}" id="module-{idx}" style="{display_style}">
        <span class="tag">{m["tag"]}</span>
        <h2>{m["title"]}</h2>
        <p>{m["intro"]}</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          {m["scenario"]}
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          {steps_html}
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-{idx}')">📋 複製本單元操作步驟</button>
        </div>
      </div>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{tool_name} 進階功能與教學應用 (互動網頁版)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: {bg_color};
      --primary-dark: {border_color};
      --primary-light: #e8f0fe;
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
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
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
      <h1>{icon} {tool_name} 進階功能與教學應用</h1>
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
      <div class="sidebar-heading">實務演練選單</div>
      {menu_items}
    </nav>

    <!-- Main Content Area -->
    <main class="content-area">
      {module_cards}
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

    fpath = os.path.join(root, file_name)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully generated {file_name}")

# 1. Google Calendar App
calendar_modules = [
    {
        "icon": "📅",
        "nav_title": "預約時間表 (Appointment Schedule)",
        "tag": "演練一：親師面談自動化",
        "title": "親師面談預約時間表設定與公開 URL 發布",
        "intro": "使用 Google Calendar 的『預約時間表』建立可供家長預約的時間區塊，系統會自動在日曆上顯示可用時段並防止衝突。",
        "scenario": "您需要在下學期舉辦全班親師面談。為了讓家長能夠彈性選擇適合的時間，並避免人工協調撞期，您需要設定一個自動化的預約介面，並複製公開連結發送給所有家長。",
        "steps": [
          "開啟 Google Calendar 點選左上角「建立 $\\rightarrow$ 預約時間表 (Appointment schedule)」。",
          "輸入預約活動標題（如：親師面談預約），設定單次面談時間長度（如 20 分鐘）。",
          "設定開放預約的日期範圍與每週可予約時間區塊。",
          "儲存後點選「分享」，複製公開預約網址 (URL) 發送給家長。"
        ]
    },
    {
        "icon": "📹",
        "nav_title": "跨校視訊與直播 (Live Streaming)",
        "tag": "演練二：大型跨校研習與直播",
        "title": "Calendar 活動排定、Google Meet 視訊與串流直播開啟",
        "intro": "排定全學期跨校活動，並在行事曆中一鍵開啟 Google Meet 視訊會議與 Live Stream 直播功能。",
        "scenario": "您正與其他學校的老師共同規劃一個全年的跨校學生交流計畫，並預計邀請外部專家進行一場開放全校觀看的線上講座。",
        "steps": [
          "在 Calendar 中選擇目標日期（如：下週五 3:00 PM - 4:00 PM），點選建立新活動。",
          "輸入活動名稱（如：Community Fair 社區展覽研討會）。",
          "點選「新增 Google Meet 視訊會議 (Add Google Meet video conferencing)」。",
          "點選 Meet 視訊下拉選單，開啟「新增串流直播 (Add live stream)」選單。"
        ]
    },
    {
        "icon": "🔒",
        "nav_title": "活動地點、提醒與與會者權限",
        "tag": "演練三：活動細節與安全性防護",
        "title": "設定活動地點、 Email 通知提醒與精確與會者權限防護",
        "intro": "在行事曆活動中加入實體地點、設定 Email 提醒，並保護活動隱私，限制受邀者修改或檢視名單。",
        "scenario": "您正在舉辦一場社區公聽會活動，需要為所有受邀專家設定 Email 提醒，並限制受邀者不能自行邀請其他人或查看完整受邀名單。",
        "steps": [
          "在活動編輯彈窗中，於地點欄位輸入精確地址（如：123 Main Street）。",
          "在通知設定中將預設通知改為「Email」，時間設定為活動前「1 小時 (1 hour before)」。",
          "在「與會者權限 (Guest permissions)」區塊中，取消勾選「邀請他人 (Invite others)」。",
          "取消勾選「檢視與會者名單 (See guest list)」，保護與會個資並儲存。"
        ]
    }
]
build_app('calendar_workshop_app.html', 'Google Calendar', '📅', '#4285f4', '#1967d2', calendar_modules)

# 2. Google Classroom App
classroom_modules = [
    {
        "icon": "🏫",
        "nav_title": "建立課程與團隊協同 (Co-teachers)",
        "tag": "演練一：課程建置與協同教學",
        "title": "建立 Classroom 課程、批次邀請學生與新增協同教師",
        "intro": "建立全新的 Classroom 空間，從試算表批次邀請學生與跨校備課夥伴，一同協同管理班級。",
        "scenario": "您要開辦一門跨班翻轉學習課程『Flipped Class』，並邀請同科目的另一位老師共同教學與批改作業。",
        "steps": [
          "進入 Google Classroom 點選右上角 <code>+</code> 選擇「建立課程」，課程名稱精確輸入「Flipped Class」。",
          "開啟包含名單的試算表 (5th Grade List)，複製學員 Email。",
          "進入 Classroom「成員 (People)」頁面，在學生區塊點選「邀請學生」並貼上 Email。",
          "在教師區塊點選「邀請教師」，輸入夥伴 Email 加入為「協同教師 (Co-teachers)」。"
        ]
    },
    {
        "icon": "📚",
        "nav_title": "單元主題與多元課堂作業建置",
        "tag": "演練二：教材結構化與作業派發",
        "title": "建立主題分頁 (Topics)、一般作業與線上閱讀素材",
        "intro": "利用「主題」將課堂素材分類為單元，並建立具體配分與截止日期的課堂作業。",
        "scenario": "您需要將課程劃分為 Term 1 與 Term 2 兩個學習主題，並在 Term 1 發布第一單元的作業與參考資料。",
        "steps": [
          "點選「課堂作業 (Classwork)」頁籤，點選「建立 $\\rightarrow$ 主題 (Topic)」，分別建立「Term 1」與「Term 2」。",
          "點選「建立 $\\rightarrow$ 作業 (Assignment)」，輸入標題「Unit 1」，總分設為 10 分，主題選擇「Term 1」。",
          "點選「建立 $\\rightarrow$ 資料 (Material)」，輸入標題「Unit 1 Readings」並附加 Docs 檔案。",
          "點選「訊息串 (Stream)」，發布含 Google Meet 連結與 4 條班級守則的歡迎公告。"
        ]
    },
    {
        "icon": "📝",
        "nav_title": "測驗作業成績匯入與原創性比對",
        "tag": "演練三：評量自動化與學術誠信",
        "title": "建立測驗作業 (Quiz Assignment) 開啟成績匯入與原創性檢查",
        "intro": "自動將 Google 表單測驗分數帶入 Classroom 成績冊，並提供作業抄襲檢查機制。",
        "scenario": "您希望在單元結束後進行線上測驗，讓分數自動帶入成績冊；同時在學生繳交報告前，讓學生能自主進行論文抄襲比對。",
        "steps": [
          "點選「建立 $\\rightarrow$ 測驗作業 (Quiz Assignment)」，輸入測驗標題。",
          "確認右側控制面板中的<strong>「成績匯入 (Grade importing)」</strong>開關已切換為開啟。",
          "在作業編輯面板下方，勾選<strong>「檢查原創性 (Originality reports)」</strong>小方塊。",
          "點選發布作業，學生繳交前即可自主進行最多 3 次原創性比對。"
        ]
    }
]
build_app('classroom_workshop_app.html', 'Google Classroom', '🏫', '#0f9d58', '#0b8043', classroom_modules)

# 3. Google Slides App
slides_modules = [
    {
        "icon": "🎨",
        "nav_title": "互動選擇板與單字記憶卡 (Hyperlink)",
        "tag": "演練一：互動投影片與頁面跳轉",
        "title": "物件與文字超連結 (Hyperlink Slides) 製作單字記憶卡",
        "intro": "利用投影片之間的超連結跳轉，製作雙向互動的 Choice Board (選擇板) 或單字記憶卡 (Flash cards)。",
        "scenario": "您希望學生為即將到來的考試製作單字記憶卡，第一張投影片呈現單字與選項，點選後能跳轉至顯示答案與定義的指定投影片。",
        "steps": [
          "開啟 Google Slides 簡報，選取投影片上的單字按鈕或文字區塊。",
          "點選頂部選單「插入 $\\rightarrow$ 連結」（或按右鍵選取「連結」）。",
          "在連結跳出視窗中，選取<strong>「簡報中的投影片 (Slides in this presentation)」</strong>。",
          "選取目標答案投影片頁碼並點選套用，實現點選按鈕自動跳轉。"
        ]
    },
    {
        "icon": "🖼️",
        "nav_title": "主題建構工具與媒體預留位置",
        "tag": "演練二：版型設計與規範建立",
        "title": "使用主題建構工具 (Theme Builder) 插入圖片預留位置 (Placeholder)",
        "intro": "透過 Theme Builder 設計全套簡報母版，並為全校或學生建立統一的圖片上傳預留框。",
        "scenario": "您正在為團隊建立一套歡迎簡報『Welcome to Our Team』，需要設計標準的教師介紹頁面，並設置格式統一的圖片預留區。",
        "steps": [
          "建立新簡報命名為「Welcome to Our Team」，首頁插入標誌圖片。",
          "點選頂部選單<strong>「檢視 $\\rightarrow$ 主題建構工具 (Theme builder)」</strong>進入母版模式。",
          "在版型中點選<strong>「插入 $\\rightarrow$ 預留位置 $\rightarrow$ 圖片預留位置 (Image placeholder)」</strong>。",
          "繪製圖片預留框並調整邊框樣式，關閉主題建構工具回主編輯頁。"
        ]
    },
    {
        "icon": "🎬",
        "nav_title": "內嵌影音與批註指派 (+Email Assign)",
        "tag": "演練三：多媒體整合與團隊任務",
        "title": "簡報內嵌 YouTube 影片與註解 `+Email` 指派審閱任務",
        "intro": "直接在 Slides 中播放影音免跳出視訊，並透過註解指派任務給團隊成員。",
        "scenario": "您需要將新的教師介紹影片嵌入簡報，並在簡報段落中新增註解指派給夥伴，要求夥伴在發布前審閱影音順暢度。",
        "steps": [
          "在目標投影片點選選單<strong>「插入 $\\rightarrow$ 影片 (Video)」</strong>，選取影音檔案「Meet Our Amazing New Teachers.mp4」。",
          "調整影片大小並在右側面板設定自動播放或起訖時間。",
          "選取簡報中的文字或影片元件，點選右側「新增註解 (Add comment)」。",
          "輸入 <strong><code>+成員Email</code></strong>（例如 <code>+teacher1@example.com</code>），並<strong>勾選「指派給... (Assign to...)」</strong>小方塊。"
        ]
    }
]
build_app('slides_workshop_app.html', 'Google Slides', '🎨', '#f4b400', '#f09300', slides_modules)

# 4. Google Sites App
sites_modules = [
    {
        "icon": "🌐",
        "nav_title": "學生專題作品集 (Subpages)",
        "tag": "演練一：多工具整合學習歷程",
        "title": "建立 Google Sites 網站並為每位學生新增專屬子頁面",
        "intro": "Google Sites 是最佳的跨工具展示容器，能將 Docs、Slides、YouTube 等專題成果整合於同一平台。",
        "scenario": "學生進行了 PBL 專題導向學習，使用了 Docs 報告、Slides 簡報與 YouTube 影片。您需要提供一個整合空間，並為每位學生指派一個分享成果的頁面。",
        "steps": [
          "進入 Google Sites 點選建立全新空白網站。",
          "點選右側面板的「頁面 (Pages)」頁籤。",
          "點選底部的「+」選單，選取「新增子頁面 (Add subpage)」。",
          "輸入學生姓名或小組名稱，為每一位學生建立專屬的成果展示 Subpage。"
        ]
    },
    {
        "icon": "🔒",
        "nav_title": "網站發布與公開存取權限",
        "tag": "演練二：外部大學與校外評審審閱",
        "title": "調整 Publish 設定：網站設 Public 與文件設 Publish to the web",
        "intro": "確保外部大學評審或校外專家能無障礙瀏覽網站及內嵌的 Google 文件。",
        "scenario": "學生要在 Google Sites 上建立備審作品集展示給目標大學。若只公開網站但內嵌文件權限受限，外部評審點進去會顯示無權限。",
        "steps": [
          "點選右上角藍色<strong>「發布 (Publish)」</strong>按鈕進入設定。",
          "在「誰可以檢視我的網站」區塊點選管理，將發布的網站切換為<strong>「公開 (Public)」</strong>。",
          "回到網站內嵌的 Google Docs 文件，開啟文件點選「檔案 $\rightarrow$ 發布至網路 (Publish to the web)」。",
          "複製發布連結並確認嵌入無誤後，正式點選發布。"
        ]
    }
]
build_app('sites_workshop_app.html', 'Google Sites', '🌐', '#7b1fa2', '#4a148c', sites_modules)

# 5. Google Sheets App
sheets_modules = [
    {
        "icon": "🎨",
        "nav_title": "成績表現視覺化 (Conditional Formatting)",
        "tag": "演練一：數據視覺化與條件格式",
        "title": "條件式格式設定 (Conditional Formatting) 自動變更儲存格外觀",
        "intro": "根據自訂的數值條件（如及格/不及格），自動讓試算表格子顯示不同的背景顏色與文字格式。",
        "scenario": "您使用 Google Sheets 追蹤學生平時測驗分數，希望系統能在分數低於 60 分時自動醒目顯示紅底白字，以便快速關懷落後學生。",
        "steps": [
          "開啟包含成績數據的 Google Sheets 試算表，選取分數欄位（如 B2:B50）。",
          "點選頂部功能表<strong>「格式 $\rightarrow$ 條件式格式設定 (Conditional Formatting)」</strong>。",
          "在右側規則設定中，將格式化條件切換為「小於 (Less than)」，數值輸入「60」。",
          "在樣式設定中選擇紅底白字，點選完成即可自動視覺化標示。"
        ]
    },
    {
        "icon": "📊",
        "nav_title": "投票統計與樞紐分析 (Column stats & Pivot)",
        "tag": "演練二：大型資料統計與圖表分析",
        "title": "直行統計 (Column stats) 與 樞紐分析表 (Pivot table) 計算回應",
        "intro": "快速查看試算表欄位回應分布，並使用樞紐分析表進行多維度的交叉分類統計。",
        "scenario": "您透過 Google 表單讓全校學生投票選出最喜歡的班服顏色，並在試算表中收集了數百筆回應。您需要快速計算每個顏色獲得多少票。",
        "steps": [
          "點選投票顏色欄位頂部的字母標籤（如 C 欄）。",
          "點選選單<strong>「資料 $\rightarrow$ 直行統計 (Column stats)」</strong>，右側側邊欄即時生成選項計數與百分比直方圖。",
          "點選選單<strong>「插入 $\rightarrow$ 樞紐分析表 (Pivot table)」</strong>建立分析分頁。",
          "將「投票顏色」拖入列，將「學生 Email」拖入值，自動算出各顏色的精確總票數。"
        ]
    }
]
build_app('sheets_workshop_app.html', 'Google Sheets', '📊', '#0f9d58', '#0b8043', sheets_modules)

# 6. Google Meet App
meet_modules = [
    {
        "icon": "📞",
        "nav_title": "網路不穩定語音備援 (Join by phone)",
        "tag": "演練一：連線品質低落之備援方案",
        "title": "網路中斷時開啟「透過電話撥號加入 (Join by phone)」功能",
        "intro": "當視訊會議中成員網路頻寬不足或連線斷斷續續時，使用電話撥號收聽與發言確保對話不中斷。",
        "scenario": "您正在舉辦線上跨校開會，其中一位老師所在地網路訊號極差、語音斷斷續續。您需要指導該同仁使用電話撥號完全參與語音對話。",
        "steps": [
          "在 Google Meet 控制列下方，點選右側<strong>「其他選項 (三點圖示)」</strong>。",
          "點選選單中的<strong>「使用電話收聽及發言 (Use a phone for audio)」</strong>。",
          "畫面將顯示專屬的電話撥號號碼與 PIN 碼。",
          "使用手機撥打該號碼並輸入 PIN 碼，即可透過行動電話網路穩定參與語音對話。"
        ]
    },
    {
        "icon": "💻",
        "nav_title": "Docs/Slides 檔案內發起與加入 Meet",
        "tag": "演練二：無縫檔案內視訊協作",
        "title": "從 Google Docs/Slides 頂部工具列直接發起或加入 Meet 會議",
        "intro": "無需切換視窗，直接在編輯 Docs 文件或 Slides 簡報時與合作夥伴開起 Meet 討論細節。",
        "scenario": "您正在與客座講師共同編修簡報與文件，希望邊看著文件畫面邊進行線上視訊討論與簡報回饋。",
        "steps": [
          "開啟共同編輯的 Google Docs 或 Google Slides 檔案。",
          "點選右上角共用按鈕旁邊的 <strong>Meet 視訊圖示</strong>。",
          "點選<strong>「在此發起新會議 (Start a new meeting)」</strong>或輸入會議代碼加入。",
          "視訊畫面將浮動呈現於文件右側，實現文件與 Meet 的深度無縫協作。"
        ]
    }
]
build_app('meet_workshop_app.html', 'Google Meet', '📹', '#00897b', '#00695c', meet_modules)

# 7. Practice Sets App
practicesets_modules = [
    {
        "icon": "💡",
        "nav_title": "腳手架學習提示 (Extra Help)",
        "tag": "演練一：適性化提示與差異化學習",
        "title": "在 Practice Sets 中設定多達 10 個學習資源 (Extra Help)",
        "intro": "為題目加入文字提示或 YouTube 教學影音，當學生答題卡關時自動提供適時腳手架支援。",
        "scenario": "您使用 Practice Sets 製作數學複習題組。考量到不同學生的理解程度差異，您希望為較難的題目提供多達 10 個輔助提示資源。",
        "steps": [
          "開啟 Google Classroom 進入「練習組 (Practice sets)」建立題組。",
          "在題目下方點選<strong>「額外協助 (Extra help)」</strong>按鈕。",
          "點選「+ 新增資源」，可選擇輸入文字提示卡或搜尋並嵌入 YouTube 教學影片。",
          "最多可加入 10 個學習資源，儲存後學生卡關時即可點選查看提示。"
        ]
    },
    {
        "icon": "🔗",
        "nav_title": "教師團隊連結共享 (Link Sharing)",
        "tag": "演練二：備課團隊資源共享",
        "title": "開啟「開啟連結共用 (Turn on link sharing)」共用題組給教研團隊",
        "intro": "開啟共用連結並複製給同科備課教師，讓同仁直接匯入並在各自的 Classroom 中使用。",
        "scenario": "您與同年級老師分工製作 Practice Sets 題組。您製作完成後，需要將練習組分享給團隊同仁，以便其他人能直接檢視與使用。",
        "steps": [
          "完成 Practice Sets 題組編輯後，點選右上角的「分享 (Share)」按鈕。",
          "切換開關點選<strong>「開啟連結共用 (Turn on link sharing)」</strong>。",
          "點選<strong>「複製連結 (Copy link)」</strong>。",
          "將連結傳送給同備課團隊老師，對方開啟連結即可將題組複製一份至其 Classroom 中使用。"
        ]
    }
]
build_app('practicesets_workshop_app.html', 'Practice Sets 練習組', '📝', '#f2994a', '#d97706', practicesets_modules)

# 8. Google Forms App
forms_modules = [
    {
        "icon": "🎥",
        "nav_title": "翻轉課堂與區段跳轉 (Go to Section)",
        "tag": "演練一：翻轉教學與適性化引導",
        "title": "Forms 內嵌教學影片與依據回應跳轉區段 (Go to section based on answer)",
        "intro": "在表單中放入引導影片，並根據單選題選項自動將學生引導至對應的學習或補救區段。",
        "scenario": "您希望實施翻轉課堂 (Flipped Classroom) 模式：在 Forms 中加入教學影片後提出特定問題，答對者跳轉至進階區段，答錯者跳轉至補救說明區段。",
        "steps": [
          "開啟 Google Forms 表單，點選右側浮動工具列的「插入影片」，內嵌 YouTube 教學影音。",
          "建立單選題（如：觀看完影片後的主要概念觀念題）。",
          "點選單選題右下角的三點圖示，勾選<strong>「依據回應跳轉至不同區段 (Go to section based on answer)」</strong>。",
          "在每個選項旁邊下拉選單中，指定跳轉的目標區段，實現適性化差異化學習路徑。"
        ]
    }
]
build_app('forms_workshop_app.html', 'Google Forms', '📝', '#673ab7', '#512da8', forms_modules)

print("\nALL 8 TOOL WORKSHOP APPS SUCCESSFULLY CREATED!")
