import os

html_content = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Docs 進階功能與行政自動化研習講義 (互動網頁版)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Google Sans', 'Noto Sans TC', sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
    }

    header {
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
    }

    .header-title h1 { font-size: 1.5rem; font-weight: 700; }
    .header-title p { font-size: 0.9rem; opacity: 0.9; margin-top: 4px; }

    .nav-links { display: flex; gap: 8px; flex-wrap: wrap; }
    .nav-btn {
      text-decoration: none;
      background: rgba(255,255,255,0.2);
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }
    .nav-btn:hover { background: white; color: var(--primary); }

    .app-layout {
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
    }

    @media (max-width: 900px) {
      .app-layout { grid-template-columns: 1fr; }
    }

    .sidebar {
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      height: fit-content;
      position: sticky;
      top: 100px;
    }

    .sidebar-heading {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }

    .menu-item {
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
    }

    .menu-item:hover { background: var(--bg-body); color: var(--primary); }
    .menu-item.active { background: var(--primary-light); color: var(--primary); font-weight: 700; }

    .content-area {
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }

    .module-card { display: none; }
    .module-card.active { display: block; animation: fadeIn 0.3s ease-in-out; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .tag {
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 12px;
    }

    h2 { font-size: 1.4rem; font-weight: 700; margin-bottom: 16px; color: var(--primary-dark); }
    h3 { font-size: 1.1rem; font-weight: 700; margin: 20px 0 10px 0; color: var(--text-main); }
    p { margin-bottom: 14px; color: #3c4043; line-height: 1.7; }

    .scenario-box {
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
    }

    .scenario-box strong { color: #b06000; }

    .step-list {
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin: 20px 0;
    }

    .step-item {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 12px;
    }

    .step-item input[type="checkbox"] {
      margin-top: 5px;
      width: 18px;
      height: 18px;
      cursor: pointer;
    }

    .action-bar {
      display: flex;
      gap: 12px;
      margin-top: 24px;
    }

    .btn {
      border: none;
      padding: 10px 20px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-primary { background: var(--primary); color: white; }
    .btn-primary:hover { background: var(--primary-dark); }
    .btn-secondary { background: var(--primary-light); color: var(--primary); }
    .btn-secondary:hover { background: #d2e3fc; }

    .toast {
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
    }
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>📄 Google Docs 進階功能與行政自動化研習講義</h1>
      <p>工具篇 (一) ｜ 實務情境演練 ‧ 隱形考點融合 ‧ 步驟互動清單</p>
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
      <div class="module-card active" id="module-0">
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

      <!-- MODULE 1 -->
      <div class="module-card" id="module-1">
        <span class="tag">核心功能演練一</span>
        <h2>智慧型畫布 (Smart Canvas) 與團隊任務指派</h2>
        <p>在 Google Docs 中輸入 <code>@</code> 符號，即可觸發「智慧型畫布」快捷選單。這能讓文件從單純的文字編輯器，升級為動態的團隊專案管理中心。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          您正在為校內專案團隊編輯一份活動會議議程文件。為了讓團隊學生與教師能清楚知道各自負責的硬體準備工作，您需要為不同任務指派具體負責人，並訂定各項任務的完成截止期限。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m1-s1">
            <label for="m1-s1">開啟會議議程 Docs 文件，移至「任務分工表」區段。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s2">
            <label for="m1-s2">在「負責人」欄位輸入 <code>@</code>，選取並插入 <strong><code>@People</code> (人員晶片)</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s3">
            <label for="m1-s3">在「預計完成日」欄位輸入 <code>@</code>，選取並插入 <strong><code>@Date</code> (日期晶片)</strong>。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-1')">📋 複製本單元操作步驟</button>
        </div>
      </div>

      <!-- MODULE 2 -->
      <div class="module-card" id="module-2">
        <span class="tag">核心功能演練二</span>
        <h2>結構化排版與動態導覽目錄 (Paragraph Styles)</h2>
        <p>要讓長篇文件自動生成方便點選跳轉的目錄，必須正確套用「段落樣式 (Paragraph Styles)」（如：標題 1、標題 2），而不是單純手動放大字體。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          您正在準備一份長篇的「角色扮演教學劇本」與「全學期課程大綱」。您希望建立一份結構嚴謹的文件，讓學生開啟檔案時，能透過最上方的目錄快速點選跳轉至自己被指派的角色部分。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m2-s1">
            <label for="m2-s1">選取劇本中的各角色名稱（如「角色 A：說書人」）。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s2">
            <label for="m2-s2">在工具列將段落樣式切換套用為 <strong><code>標題 1 (Heading 1)</code></strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s3">
            <label for="m2-s3">移至文件開頭的第一頁，點選選單 <strong>「插入 $\rightarrow$ 目錄 (Table of Contents)」</strong>。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-2')">📋 複製本單元操作步驟</button>
        </div>
      </div>

      <!-- MODULE 3 -->
      <div class="module-card" id="module-3">
        <span class="tag">核心功能演練三</span>
        <h2>高效內文檢索與批次修正 (Find and Replace)</h2>
        <p>在整理多頁報告或教學素材時，使用快捷鍵 <code>Ctrl + H</code> 可在數秒內完成全篇文件的搜尋與取代。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          學生完成了一份多頁的研究報告後，突然發現自己在好幾個不同段落裡，都將引用的學者名字拼錯了。學生需要快速找到所有寫錯的名字並一次性全部修正。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m3-s1">
            <label for="m3-s1">在 Google Docs 中按下快捷鍵 <strong><code>Ctrl + H</code></strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s2">
            <label for="m3-s2">在「尋找」欄位輸入拼錯的名字，在「替換為」欄位輸入正確的名字。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s3">
            <label for="m3-s3">點選 <strong>「全部替換 (Replace All)」</strong> 一鍵更正。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-3')">📋 複製本單元操作步驟</button>
        </div>
      </div>

      <!-- MODULE 4 -->
      <div class="module-card" id="module-4">
        <span class="tag">核心功能演練四</span>
        <h2>跨語言親師溝通與文件一鍵翻譯 (Translate Document)</h2>
        <p>Google Docs 內建機器翻譯引擎，免安裝外掛即可將全篇文件複製並翻譯為全球數十種語言。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          身為導師，您每週都會編寫「班級每週學習通訊」發送給家長。為了讓班上不同母語背景（如越南語、印尼語、英語等）的家長也能無障礙閱讀班級動態，您需要快速產出不同語言版本的文件。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m4-s1">
            <label for="m4-s1">開啟中文「班級每週通訊」Docs 文件。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s2">
            <label for="m4-s2">點選頂部功能表 <strong>「工具 $\rightarrow$ 翻譯文件 (Translate Document)」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s3">
            <label for="m4-s3">選取目標語言（如越南語）並點選「翻譯」，生成雙語新文件。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-4')">📋 複製本單元操作步驟</button>
        </div>
      </div>

      <!-- MODULE 5 -->
      <div class="module-card" id="module-5">
        <span class="tag">核心功能演練五</span>
        <h2>非同步語音註解與多媒體回饋 (Marketplace Add-ons)</h2>
        <p>若希望針對學生的作文或作業給予更具親和力、非同步的「口頭/語音回饋」，可透過 Workspace Marketplace 安裝第三方擴充功能 (如 Mote)。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          學生在 Google Docs 提交了作文作業後，老師希望除了文字批改外，還能錄製一段親切的口頭語音說明，給予學生非同步的口頭回饋與建議。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m5-s1">
            <label for="m5-s1">點選選單 <strong>「擴充功能 $\rightarrow$ 外掛程式 $\rightarrow$ 取得外掛程式」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m5-s2">
            <label for="m5-s2">在 Marketplace 搜尋並安裝語音回饋外掛 (如 Mote)。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m5-s3">
            <label for="m5-s3">在學生作業新增註解並點選「語音錄音」發布聲音回饋。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-5')">📋 複製本單元操作步驟</button>
        </div>
      </div>

      <!-- MODULE 6 -->
      <div class="module-card" id="module-6">
        <span class="tag">核心功能演練六</span>
        <h2>跨軟體行政整合 (行事曆與簡報批註連動)</h2>
        <p>Google Docs 能與 Calendar 及 Slides 深度連動，實現一鍵開立會議紀錄與批註指派任務。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          團隊正在進行教學專案討論，需要建立一份會議紀錄供所有人共同編輯，並在討論結束後將特定修改任務精確指派給特定成員。
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m6-s1">
            <label for="m6-s1">在 Calendar 活動視窗點選 <strong>「新增會議紀錄 (Add meeting notes)」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m6-s2">
            <label for="m6-s2">在 Docs 或簡報內選取段落新增註解，輸入 <strong><code>+成員Email</code></strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m6-s3">
            <label for="m6-s3"><strong>勾選「指派給... (Assign to...)」</strong>核取方塊並點選指派。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-6')">📋 複製本單元操作步驟</button>
        </div>
      </div>

    </main>
  </div>

  <div class="toast" id="toast">已複製操作步驟至剪貼簿！</div>

  <script>
    function showModule(idx) {
      document.querySelectorAll('.menu-item').forEach((btn, i) => {
        btn.classList.toggle('active', i === idx);
      });
      document.querySelectorAll('.module-card').forEach((card, i) => {
        card.classList.toggle('active', i === idx);
      });
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function copySteps(modId) {
      const mod = document.getElementById(modId);
      const title = mod.querySelector('h2').innerText;
      const steps = Array.from(mod.querySelectorAll('.step-item label'))
        .map((l, i) => `${i + 1}. ${l.innerText}`)
        .join('\\n');
      
      const text = `【${title}】\\n${steps}`;
      navigator.clipboard.writeText(text).then(() => {
        const toast = document.getElementById('toast');
        toast.style.display = 'block';
        setTimeout(() => toast.style.display = 'none', 2500);
      });
    }
  </script>
</body>
</html>
'''

path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs_workshop_app.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated docs_workshop_app.html!")
