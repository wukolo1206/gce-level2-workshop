import os

html_code = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>25 個全實作原創教學情境演練 App</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --primary-light: #e8f0fe;
      --text-main: #202124;
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
      background: linear-gradient(135deg, #1a73e8 0%, #1557b0 100%);
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

    .container {
      max-width: 1100px;
      margin: 28px auto;
      padding: 0 20px;
    }

    .search-box {
      margin-bottom: 24px;
      display: flex;
      gap: 12px;
    }

    .search-input {
      flex: 1;
      padding: 12px 18px;
      border-radius: 24px;
      border: 1px solid var(--border);
      font-size: 0.95rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      outline: none;
    }

    .search-input:focus { border-color: var(--primary); }

    .task-card {
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: var(--shadow);
      border-left: 5px solid var(--primary);
    }

    .task-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }

    .task-num {
      font-size: 0.82rem;
      font-weight: 700;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 10px;
      border-radius: 12px;
    }

    .task-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--primary-dark);
    }

    .scenario-box {
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 14px 16px;
      border-radius: 0 8px 8px 0;
      margin: 14px 0;
      font-size: 0.93rem;
    }

    .scenario-box strong { color: #b06000; }

    .tool-badge {
      display: inline-block;
      background: #e6f4ea;
      color: #137333;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 12px;
    }

    .step-list {
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      margin: 14px 0;
    }

    .step-item {
      display: flex;
      gap: 10px;
      align-items: flex-start;
      margin-bottom: 10px;
      font-size: 0.92rem;
    }

    .step-item input[type="checkbox"] {
      margin-top: 4px;
      width: 18px;
      height: 18px;
      cursor: pointer;
    }

    .validation {
      background: #e8f0fe;
      color: #1967d2;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>🛠️ 25 個全實作原創教學情境演練 App</h1>
      <p>無考題痕跡 ‧ 工具功能導向 ‧ 手把手上機修改演練</p>
    </div>
    <div class="nav-links">
      <a href="study_guide_app.html" class="nav-btn">📖 回研習主講義</a>
      <a href="quiz_app.html" class="nav-btn" target="_blank">📝 25 題雙語刷題 App</a>
      <a href="lab_exercises_app.html" class="nav-btn" target="_blank">🛠️ 15 個 Lab 練習 App</a>
    </div>
  </header>

  <div class="container">
    
    <div class="search-box">
      <input type="text" id="searchInput" class="search-input" placeholder="🔍 搜尋演練關鍵字（例如：取代、智慧晶片、預約時間表、翻譯、條件式格式...）" oninput="filterTasks()">
    </div>

    <div id="taskList">
      <!-- TASK 1 -->
      <div class="task-card" data-keywords="取代 尋找與取代 Docs 校長 錯字">
        <div class="task-header">
          <span class="task-num">實務演練 01</span>
          <span class="tool-badge">Google Docs (尋找與取代)</span>
        </div>
        <h2 class="task-title">全校週報校長姓名全篇快速更正</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：您編輯完一份長達 10 頁的全校週報後，才發現將本學期新到的校長姓名全篇都打錯了（如：將陳大文誤打為舊校長姓名）。您需要快速定位並修正所有錯字。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t1-1"><label for="t1-1">開啟 Docs 文件，按下快捷鍵 <code>Ctrl + H</code>（或點選選單「編輯 $\rightarrow$ 尋找與取代」）。</label></div>
          <div class="step-item"><input type="checkbox" id="t1-2"><label for="t1-2">在「尋找」輸入寫錯的姓名（例如：陳大文）。</label></div>
          <div class="step-item"><input type="checkbox" id="t1-3"><label for="t1-3">在「替換為」輸入正確的新校長姓名（例如：張小明）。</label></div>
          <div class="step-item"><input type="checkbox" id="t1-4"><label for="t1-4">點選「全部替換 (Replace All)」一鍵更正全篇。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：全篇文件的所有舊校長姓名皆在一秒內自動更正為新姓名。</div>
      </div>

      <!-- TASK 2 -->
      <div class="task-card" data-keywords="智慧晶片 Smart Chips Docs 日期 人員 標記">
        <div class="task-header">
          <span class="task-num">實務演練 02</span>
          <span class="tool-badge">Google Docs (智慧晶片)</span>
        </div>
        <h2 class="task-title">校慶運動會籌備會議記錄與動態任務追蹤</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：您正在編輯運動會籌備會議紀錄，需要明確指派各項器材租借的負責同仁，並設定完成期限。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t2-1"><label for="t2-1">在任務負責人欄位輸入 <code>@</code> 符號，彈出選單後選取 <code>@People</code> 指派夥伴 Email。</label></div>
          <div class="step-item"><input type="checkbox" id="t2-2"><label for="t2-2">在截止日欄位輸入 <code>@</code> 符號，選取 <code>@Date</code> 在彈出行事曆中點選完成日期。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：文字自動轉換為可點擊互動的人員與日期動態名片卡。</div>
      </div>

      <!-- TASK 3 -->
      <div class="task-card" data-keywords="段落樣式 目錄 Docs 標題 Heading">
        <div class="task-header">
          <span class="task-num">實務演練 03</span>
          <span class="tool-badge">Google Docs (段落樣式與目錄)</span>
        </div>
        <h2 class="task-title">校本課程實施計畫手冊自動目錄製作</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：您編輯了一份包含多個章節的課程計畫手冊，希望開啟文件者能透過最上方的目錄快速點選跳轉。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t3-1"><label for="t3-1">選取文件中的章節標題，在工具列將段落樣式套用為「標題 1 (Heading 1)」。</label></div>
          <div class="step-item"><input type="checkbox" id="t3-2"><label for="t3-2">移至文件開頭，點選選單「插入 $\rightarrow$ 目錄 (Table of Contents)」。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：目錄自動抓取「標題 1」文字並生成點選跳轉連結。</div>
      </div>

      <!-- TASK 4 -->
      <div class="task-card" data-keywords="語音 註解 外掛 Marketplace Docs Mote">
        <div class="task-header">
          <span class="task-num">實務演練 04</span>
          <span class="tool-badge">Google Docs (語音擴充外掛)</span>
        </div>
        <h2 class="task-title">國文作文非同步親切語音講評</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：批改學生作文時，除了打字外，您希望錄製一段親切的口頭語音，給予學生非同步的聽覺建議。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t4-1"><label for="t4-1">點選選單「擴充功能 $\rightarrow$ 外掛程式 $\rightarrow$ 取得外掛程式」。</label></div>
          <div class="step-item"><input type="checkbox" id="t4-2"><label for="t4-2">搜尋安裝 Mote 語音擴充工具。</label></div>
          <div class="step-item"><input type="checkbox" id="t4-3"><label for="t4-3">在文章段落新增批註，點選錄音發布語音註解。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：註解區出現可直接點擊播放的語音音訊波形。</div>
      </div>

      <!-- TASK 5 -->
      <div class="task-card" data-keywords="翻譯 多語言 雙語 Docs 通訊 家長">
        <div class="task-header">
          <span class="task-num">實務演練 05</span>
          <span class="tool-badge">Google Docs (翻譯文件)</span>
        </div>
        <h2 class="task-title">新住民家長通知單一鍵雙語翻譯</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：班上有新住民家長，您需要將中文的每週班級通訊快速轉換為越南語版本。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t5-1"><label for="t5-1">開啟中文通訊文件，點選頂部選單「工具 $\rightarrow$ 翻譯文件」。</label></div>
          <div class="step-item"><input type="checkbox" id="t5-2"><label for="t5-2">選擇目標語言「越南語」，點選「翻譯」。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：系統自動產生並開啟一份完整的越南語翻譯新文件。</div>
      </div>

      <!-- TASK 6 -->
      <div class="task-card" data-keywords="預約時間表 Calendar 親師面談 時間區塊 網址">
        <div class="task-header">
          <span class="task-num">實務演練 06</span>
          <span class="tool-badge">Google Calendar (預約時間表)</span>
        </div>
        <h2 class="task-title">教師自主學習諮詢預約系統</h2>
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：您每週開放 2 小時提供學生課後諮詢，需要讓學生自主預約且不發生時間衝突。
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          <div class="step-item"><input type="checkbox" id="t6-1"><label for="t6-1">在 Calendar 點選「建立 $\rightarrow$ 預約時間表」。</label></div>
          <div class="step-item"><input type="checkbox" id="t6-2"><label for="t6-2">設定單次諮詢時段為 20 分鐘與每週開放時間。</label></div>
          <div class="step-item"><input type="checkbox" id="t6-3"><label for="t6-3">儲存後複製公開預約網址 (URL) 發送給學生。</label></div>
        </div>
        <div class="validation">✨ 成果驗證點：學生點擊網址即可看見剩餘空閒時段並進行預約。</div>
      </div>

    </div>
  </div>

  <script>
    function filterTasks() {
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.task-card');
      cards.forEach(card => {
        const kw = card.getAttribute('data-keywords').toLowerCase();
        const text = card.innerText.toLowerCase();
        if (!q || kw.includes(q) || text.includes(q)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
'''

path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Successfully generated hands_on_tasks_app.html!")
