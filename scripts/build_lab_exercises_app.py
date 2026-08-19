html_code = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Certified Educator Level 2 - 15 個 Lab 實作手把手練習網頁 App</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --accent: #34a853;
      --warning: #fbbc04;
      --danger: #ea4335;
      --dark: #202124;
      --light-bg: #f8f9fa;
      --card-bg: #ffffff;
      --border: #dadce0;
      --text: #3c4043;
      --text-muted: #5f6368;
      --shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      --radius: 12px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Noto Sans TC', 'Outfit', sans-serif; }

    body { background: var(--light-bg); color: var(--text); padding-bottom: 60px; line-height: 1.6; }

    header {
      background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%);
      color: white;
      padding: 24px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(26, 115, 232, 0.3);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand-title h1 { font-size: 1.4rem; font-weight: 700; }
    .brand-title p { font-size: 0.88rem; opacity: 0.9; }

    .container { max-width: 1100px; margin: 28px auto; padding: 0 16px; }

    /* Top Lab Selector Tabs */
    .lab-tabs {
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .lab-tab-btn {
      padding: 12px 24px;
      border-radius: 30px;
      border: 1.5px solid var(--border);
      background: white;
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .lab-tab-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
      box-shadow: 0 4px 12px rgba(26, 115, 232, 0.25);
    }

    .exercise-card {
      background: white;
      border-radius: var(--radius);
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
      border-left: 6px solid var(--primary);
    }

    .ex-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }

    .ex-badge {
      background: #e8f0fe;
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 16px;
      font-size: 0.85rem;
      font-weight: 700;
    }

    .ex-title { font-size: 1.25rem; font-weight: 700; color: var(--dark); margin-bottom: 12px; }

    .target-box {
      background: #f1f3f4;
      padding: 12px 16px;
      border-radius: 8px;
      font-size: 0.92rem;
      color: var(--dark);
      margin-bottom: 16px;
    }

    .orig-box {
      background: #fff8e1;
      border-left: 4px solid var(--warning);
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      font-size: 0.9rem;
      color: #795548;
      margin-bottom: 20px;
      font-family: 'Fira Code', monospace;
    }

    .steps-list { list-style: none; margin-bottom: 20px; }

    .step-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px;
      border-bottom: 1px solid var(--light-bg);
    }

    .step-item:last-child { border-bottom: none; }

    .step-check {
      width: 20px;
      height: 20px;
      margin-top: 2px;
      cursor: pointer;
    }

    .step-text { flex: 1; font-size: 0.95rem; line-height: 1.6; }

    .copy-btn {
      background: #e8f0fe;
      color: var(--primary);
      border: 1px solid #d2e3fc;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      margin-left: 6px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .copy-btn:hover { background: #d2e3fc; }

    .pitfall-box {
      background: #fce8e6;
      border-left: 4px solid var(--danger);
      padding: 14px 18px;
      border-radius: 0 8px 8px 0;
      font-size: 0.9rem;
      color: #c5221f;
    }

    .pitfall-title { font-weight: 700; margin-bottom: 4px; }
  </style>
</head>
<body>

  <header>
    <div class="brand-title">
      <h1>Google Level 2 實務操作演練 App</h1>
      <p>15 個手把手實務 Lab 演練單元 (Classroom, Calendar, Slides)</p>
    </div>
    <div>
      <a href="study_guide_app.html" style="color:white; text-decoration:none; background:rgba(255,255,255,0.2); padding:8px 16px; border-radius:20px; font-weight:700;">🔙 返回講義總網頁</a>
    </div>
  </header>

  <div class="container">

    <!-- Top Tabs -->
    <div class="lab-tabs">
      <button class="lab-tab-btn active" id="tab-lab1" onclick="switchLab('lab1')">🏫 Lab 1: Google Classroom (5 個演練)</button>
      <button class="lab-tab-btn" id="tab-lab2" onclick="switchLab('lab2')">📅 Lab 2: Google Calendar (5 個演練)</button>
      <button class="lab-tab-btn" id="tab-lab3" onclick="switchLab('lab3')">🎨 Lab 3: Google Slides (5 個演練)</button>
    </div>

    <!-- LAB 1 CONTENT -->
    <div id="view-lab1">
      
      <!-- Ex 1-1 -->
      <div class="exercise-card">
        <div class="ex-header">
          <span class="ex-badge">Lab 1 - 演練 1-1</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">建立班級 (Class Creation)</span>
        </div>
        <div class="ex-title">建立翻轉教室課程 (Flipped Class)</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握在 Google Classroom 中建立新課程並完成標準化命名。</div>
        <div class="orig-box">📋 官方原題指令：Create a class named `Flipped Class`.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">開啟 <a href="https://classroom.google.com" target="_blank">Google Classroom</a> 網頁。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選右上角的 <strong>「＋」</strong> 圖示，選擇 <strong>「建立課程 (Create class)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在「課程名稱 (Class name)」欄位精確輸入：<code>Flipped Class</code> <button class="copy-btn" onclick="copyText('Flipped Class')">📋 複製文字</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選右下角 <strong>「建立」</strong>。建立完成後點擊評分系統之 <strong>Check my progress</strong>。</div>
          </li>
        </ul>
        <div class="pitfall-box">
          <div class="pitfall-title">💡 評分檢核與防踩坑提醒：</div>
          課程名稱必須精確為 <code>Flipped Class</code>（包含大小寫與空格），切勿輸入中文「翻轉教室」，否則評分系統無法識別。
        </div>
      </div>

      <!-- Ex 1-2 -->
      <div class="exercise-card">
        <div class="ex-header">
          <span class="ex-badge">Lab 1 - 演練 1-2</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">邀請成員 (Member Invitations)</span>
        </div>
        <div class="ex-title">從試算表批量邀請協同教師與學生</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會從 Google Sheets 讀取 Email 清單，區分「協同教師 (Co-teacher)」與「學生 (Student)」進行邀請。</div>
        <div class="orig-box">📋 官方原題指令：Utilize email IDs from `5th Grade List` spreadsheet to invite co-teachers and students.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">開啟 Google Drive，尋找並開啟名為 <code>5th Grade List</code> 的 Google 試算表。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">複製試算表中 Teacher 欄位的 Email；回到 Classroom 進入 <strong>「成員 (People)」</strong> 頁籤。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在「教師 (Teachers)」右側點選邀請圖示，貼上 Email 邀請為 <strong>協同教師 (Co-teacher)</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">複製 Student 欄位 Email；在「學生 (Students)」右側點選邀請圖示，貼上 Email 完成學生邀請。</div>
          </li>
        </ul>
        <div class="pitfall-box">
          <div class="pitfall-title">💡 評分檢核與防踩坑提醒：</div>
          注意教師與學生必須分開貼至對應的 Teachers 與 Students 欄位，否則身份會錯置。
        </div>
      </div>

      <!-- Ex 1-3 -->
      <div class="exercise-card">
        <div class="ex-header">
          <span class="ex-badge">Lab 1 - 演練 1-3</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">主題管理 (Topic Management)</span>
        </div>
        <div class="ex-title">建構學期主題架構 (Term 1 & Term 2)</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會在「課堂作業」中建立結構化的主題分類。</div>
        <div class="orig-box">📋 官方原題指令：Create two topics named `Term 1` and `Term 2`, respectively.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">切換至 <strong>「課堂作業 (Classwork)」</strong> 頁籤。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選 <strong>「＋建立 (＋Create) $\rightarrow$ 主題 (Topic)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">輸入第一個主題名稱：<code>Term 1</code> <button class="copy-btn" onclick="copyText('Term 1')">📋 複製文字</button>，點選「新增」。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">再次點選「＋建立 $\rightarrow$ 主題」，輸入第二個主題名稱：<code>Term 2</code> <button class="copy-btn" onclick="copyText('Term 2')">📋 複製文字</button>，點選「新增」。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 1-4 -->
      <div class="exercise-card">
        <div class="ex-header">
          <span class="ex-badge">Lab 1 - 演練 1-4</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">作業與教材 (Assignment & Material)</span>
        </div>
        <div class="ex-title">建立與指派配分作業及教材</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握作業設定（配分、截止日、主題、附件）與教材發布。</div>
        <div class="orig-box">📋 官方原題指令：1. Assignment `Unit 1`, file `5th Grade Poetic Devices`, Points: `10`, Due: `next week`, Topic: `Term 1`. 2. Material `Unit 1 Readings`, file `5th Grade Poetry: Unit 1 Reading List`.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「＋建立 $\rightarrow$ 作業」。標題輸入 <code>Unit 1</code>，夾帶 Drive 檔案 <code>5th Grade Poetic Devices</code>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">右側設定：得分設為 <code>10</code> 分，截止日期設定為 <code>下週同一天</code>，主題選取 <code>Term 1</code>，點選 <strong>「出題 (Assign)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「＋建立 $\rightarrow$ 教材 (Material)」。標題輸入 <code>Unit 1 Readings</code>，夾帶 Drive 檔案 <code>5th Grade Poetry: Unit 1 Reading List</code>，點選 <strong>「發布 (Post)」</strong>。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 1-5 -->
      <div class="exercise-card">
        <div class="ex-header">
          <span class="ex-badge">Lab 1 - 演練 1-5</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">公告與 Meet (Announcements)</span>
        </div>
        <div class="ex-title">發布整合 Meet 連結與守則之班級公告</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會在訊息串發布含 Meet 連結與條列守則的公告。</div>
        <div class="orig-box">📋 官方原題指令：Description: `Reminder: You have an upcoming online session.`, Include Meet link. Rules: `Arrive on time; Keep mics muted; Raise hands to speak.`</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">切換至 <strong>「訊息串 (Stream)」</strong>，點選「宣布事項」。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">輸入內文：<code>Reminder: You have an upcoming online session.</code> <button class="copy-btn" onclick="copyText('Reminder: You have an upcoming online session.')">📋 複製</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">輸入守則：<code>Arrive on time; Keep mics muted; Raise hands to speak.</code> <button class="copy-btn" onclick="copyText('Arrive on time; Keep mics muted; Raise hands to speak.')">📋 複製</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「新增 Google Meet 連結」按鈕，點選 <strong>「發布 (Post)」</strong>。</div>
          </li>
        </ul>
      </div>

    </div>

    <!-- LAB 2 CONTENT -->
    <div id="view-lab2" style="display:none;">
      
      <!-- Ex 2-1 -->
      <div class="exercise-card" style="border-left-color:var(--warning);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fef7e0; color:#b06000;">Lab 2 - 演練 2-1</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">活動與附件 (Event & Attachment)</span>
        </div>
        <div class="ex-title">建立混合式活動與雲端硬碟附件</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會在 Google 日曆中設定精確時段活動並附加雲端硬碟檔案。</div>
        <div class="orig-box">📋 官方原題指令：Title: `Community Fair`, Time: `3pm to 4pm next Friday`, Attach `Community Fair Agenda` from Drive.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">開啟 <a href="https://calendar.google.com" target="_blank">Google Calendar</a>，導覽至下週五 (Next Friday)。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在 <strong>15:00 - 16:00 (3pm to 4pm)</strong> 時段點選建立活動。標題輸入：<code>Community Fair</code> <button class="copy-btn" onclick="copyText('Community Fair')">📋 複製</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「新增說明或附件」 $\rightarrow$ 附件 (紙夾圖示)，選取 Drive 中的 <code>Community Fair Agenda</code> 檔案。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 2-2 -->
      <div class="exercise-card" style="border-left-color:var(--warning);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fef7e0; color:#b06000;">Lab 2 - 演練 2-2</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">串流直播 (Live Streaming)</span>
        </div>
        <div class="ex-title">設定 Google Meet 串流直播功能</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握 Google Meet 視訊會議的「串流直播 (Live Stream)」進階設定。</div>
        <div class="orig-box">📋 官方原題指令：Allow guests to join via Google Meet. Enable guests to attend with live streaming.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在活動編輯視窗中，點選 <strong>「新增 Google Meet 視訊會議」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選 Meet 旁之 <strong>齒輪圖示 (Video call options)</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">找到「串流 (Live Stream)」頁籤，點選 <strong>「新增串流 (Add stream)」</strong>，儲存設定。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 2-3 -->
      <div class="exercise-card" style="border-left-color:var(--warning);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fef7e0; color:#b06000;">Lab 2 - 演練 2-3</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">活動地點 (Location)</span>
        </div>
        <div class="ex-title">標註實體活動地點 (123 Main Street)</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會在日曆活動中加入精確地圖定位。</div>
        <div class="orig-box">📋 官方原題指令：Add location as `123 Main Street`.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在活動編輯欄位點選 <strong>「新增地點 (Add location)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">輸入地址：<code>123 Main Street</code> <button class="copy-btn" onclick="copyText('123 Main Street')">📋 複製</button></div>
          </li>
        </ul>
      </div>

      <!-- Ex 2-4 -->
      <div class="exercise-card" style="border-left-color:var(--warning);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fef7e0; color:#b06000;">Lab 2 - 演練 2-4</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">提醒通知 (Email Notifications)</span>
        </div>
        <div class="ex-title">設定 1 小時前 Email 電子郵件提醒</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>區分彈窗通知與 Email 通知，設定精確倒數時長。</div>
        <div class="orig-box">📋 官方原題指令：Set personal notification to alert attendees 1 hour via email before event.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在活動編輯畫面中找到「通知 (Notification)」設定，點選新增通知。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">通知類型從預設 Notification 切換為 <strong>「電子郵件 (Email)」</strong>，時間設為 <strong>`1 小時前 (1 hour)`</strong>。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 2-5 -->
      <div class="exercise-card" style="border-left-color:var(--warning);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fef7e0; color:#b06000;">Lab 2 - 演練 2-5</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">與會者隱私 (Guest Permissions)</span>
        </div>
        <div class="ex-title">批量邀請與會者並限制隱私權限</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握「禁止再邀請 (Invite others)」與「隱藏名單 (See guest list)」之親師隱私設定。</div>
        <div class="orig-box">📋 官方原題指令：Invite guests from `Community Fair Invite List`. Guests cannot invite others & cannot see other guests' emails.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">開啟 Drive 的 <code>Community Fair Invite List</code> 試算表，複製 Email 名單貼至日曆「新增與會者」。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在「與會者權限 (Guest permissions)」欄位：</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">❌ <strong>取消勾選「邀請其他人 (Invite others)」</strong></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">❌ <strong>取消勾選「檢視與會者清單 (See guest list)」</strong>，點選「儲存」。</div>
          </li>
        </ul>
        <div class="pitfall-box">
          <div class="pitfall-title">💡 評分核心考點：</div>
          取消勾選 Invite others 與 See guest list 是自動評分的最重要指標，請務必確定這兩項勾選已取消！
        </div>
      </div>

    </div>

    <!-- LAB 3 CONTENT -->
    <div id="view-lab3" style="display:none;">
      
      <!-- Ex 3-1 -->
      <div class="exercise-card" style="border-left-color:var(--danger);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fce8e6; color:#c5221f;">Lab 3 - 演練 3-1</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">封面與圖片 (Title Slide & Image)</span>
        </div>
        <div class="ex-title">建立簡報封面與插入 Drive 圖片</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會建立 Google 簡報並從雲端硬碟插入封面圖片。</div>
        <div class="orig-box">📋 官方原題指令：Create presentation `Welcome to Our Team`. Insert image `handclap.png` from Drive.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">開啟 <a href="https://slides.google.com" target="_blank">Google Slides</a> 建立新簡報。檔名與封面標題皆輸入：<code>Welcome to Our Team</code> <button class="copy-btn" onclick="copyText('Welcome to Our Team')">📋 複製</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「插入 $\rightarrow$ 圖片 $\rightarrow$ 雲端硬碟」，選取 <code>handclap.png</code> 圖片插入至封面頁。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 3-2 -->
      <div class="exercise-card" style="border-left-color:var(--danger);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fce8e6; color:#c5221f;">Lab 3 - 演練 3-2</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">主題預留位置 (Theme Builder)</span>
        </div>
        <div class="ex-title">製作教師簡介頁面與編輯主題圖片預留位置</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握簡報內文貼上樣版與「主題建構工具 (Theme Builder)」新增圖片預留位置。</div>
        <div class="orig-box">📋 官方原題指令：Add 3 slides (Teacher 1/2/3). Edit Theme Builder: create layout `Image Placeholder` and add rectangular image placeholder.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">新增 3 張 Title & Body 投影片，標題設為 Teacher 1, Teacher 2, Teacher 3。內文直接輸入資訊欄位。共用給 Teacher 1/2/3 設定為 Editor。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選 <strong>「檢視 $\rightarrow$ 主題建構工具 (Theme builder)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">新增版面配置，重新命名為 <code>Image Placeholder</code> <button class="copy-btn" onclick="copyText('Image Placeholder')">📋 複製</button></div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選「插入 $\rightarrow$ 預留位置 $\rightarrow$ 圖片預留位置」，畫一矩形。關閉主題建構工具，新增投影片套用該版面。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 3-3 -->
      <div class="exercise-card" style="border-left-color:var(--danger);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fce8e6; color:#c5221f;">Lab 3 - 演練 3-3</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">批註指派 (Assign via Comments)</span>
        </div>
        <div class="ex-title">運用批註功能進行任務指派</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握在簡報中透過批註以 `+Email` 將指定投影片「指派 (Assign)」給成員。</div>
        <div class="orig-box">📋 官方原題指令：Assign slides via comments: Schedule (Teacher 1), Expectations (Teacher 1), Field Trips (Teacher 2), Academic Support (Teacher 2), Documents (Teacher 3).</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">新增 5 張投影片，標題分別輸入：Schedule, Classroom Expectations, Field Trips, Academic Support, Important Documents。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">在各頁按 <code>Ctrl+Alt+M</code> 新增批註，輸入 <code>+Teacher Email</code>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">⚠️ <strong>務必手動勾選「指派給... (Assign to...)」小方塊！</strong> 點選「指派」。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 3-4 -->
      <div class="exercise-card" style="border-left-color:var(--danger);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fce8e6; color:#c5221f;">Lab 3 - 演練 3-4</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">內嵌影片 (Video Insertion)</span>
        </div>
        <div class="ex-title">內嵌雲端硬碟影音媒體</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>學會在 Google 簡報中直接插入 Drive 裡面的影音媒體檔案。</div>
        <div class="orig-box">📋 官方原題指令：Insert video `Meet Our Amazing New Teachers.mp4` from Google Drive into a blank new slide.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">新增一張空白投影片 (Blank slide)。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選 <strong>「插入 (Insert) $\rightarrow$ 影片 (Video)」</strong>。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">切換至 <strong>「Google 雲端硬碟」</strong> 分頁，選取 <code>Meet Our Amazing New Teachers.mp4</code> 影片插入。</div>
          </li>
        </ul>
      </div>

      <!-- Ex 3-5 -->
      <div class="exercise-card" style="border-left-color:var(--danger);">
        <div class="ex-header">
          <span class="ex-badge" style="background:#fce8e6; color:#c5221f;">Lab 3 - 演練 3-5</span>
          <span style="font-size:0.85rem; color:var(--text-muted);">主管審閱 (Commenter Access)</span>
        </div>
        <div class="ex-title">設定主管審閱註解者權限</div>
        <div class="target-box"><strong>🎯 學習目標：</strong>掌握精確的權限控管，將簡報分享給主管進行「註解 (Commenter)」審閱。</div>
        <div class="orig-box">📋 官方原題指令：Share presentation with Education leader with Commenter access.</div>
        <ul class="steps-list">
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">點選右上角 <strong>「共用 (Share)」</strong> 按鈕。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">輸入 `Education leader` 的電子郵件地址。</div>
          </li>
          <li class="step-item">
            <input type="checkbox" class="step-check">
            <div class="step-text">權限切換為 <strong>「註解者 (Commenter)」</strong>，點選「發送」。</div>
          </li>
        </ul>
      </div>

    </div>

  </div>

  <script>
    function switchLab(lab) {
      document.querySelectorAll('.lab-tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById('view-lab1').style.display = 'none';
      document.getElementById('view-lab2').style.display = 'none';
      document.getElementById('view-lab3').style.display = 'none';

      document.getElementById('tab-' + lab).classList.add('active');
      document.getElementById('view-' + lab).style.display = 'block';
    }

    function copyText(str) {
      navigator.clipboard.writeText(str).then(() => {
        alert('已成功複製關鍵字：\"' + str + '\"');
      });
    }
  </script>
</body>
</html>
"""

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\lab_exercises_app.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('Successfully generated lab_exercises_app.html!')
