import json, os

links_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\all_25_real_workspace_links.json'
with open(links_path, 'r', encoding='utf-8') as f:
    links_data = json.load(f)

print(f"Loaded {len(links_data)} real links!")

tasks_data = [
    {
        "num": "01", "key": "Task 01", "tool": "Google Docs (尋找與取代)", "title": "全校週報校長姓名全篇快速更正", "kw": "取代 尋找與取代 Docs 校長 錯字",
        "scenario": "您編輯完一份長達 10 頁的全校週報後，才發現將本學期新到的校長姓名全篇都打錯了（如：將陳大文誤打為舊校長姓名）。您需要快速定位並修正所有錯字。",
        "steps": ["開啟 Docs 文件，按下快捷鍵 Ctrl + H（或點選選單「編輯 -> 尋找與取代」）。", "在「尋找」輸入寫錯的姓名（例如：陳大文）。", "在「替換為」輸入正確的新校長姓名（例如：張小明）。", "點選「全部替換 (Replace All)」一鍵更正全篇。"],
        "val": "全篇文件的所有舊校長姓名皆在一秒內自動更正為新姓名。"
    },
    {
        "num": "02", "key": "Task 02", "tool": "Google Docs (智慧晶片)", "title": "校慶運動會籌備會議記錄與動態任務追蹤", "kw": "智慧晶片 Smart Chips Docs 日期 人員 標記",
        "scenario": "您正在編輯運動會籌備會議紀錄，需要明確指派各項器材租借的負責同仁，並設定完成期限。",
        "steps": ["在任務負責人欄位輸入 @ 符號，彈出選單後選取 @People 指派夥伴 Email。", "在截止日欄位輸入 @ 符號，選取 @Date 在彈出行事曆中點選完成日期。"],
        "val": "文字自動轉換為可點擊互動的人員與日期動態名片卡。"
    },
    {
        "num": "03", "key": "Task 03", "tool": "Google Docs (段落樣式與目錄)", "title": "校本課程實施計畫手冊自動目錄製作", "kw": "段落樣式 目錄 Docs 標題 Heading",
        "scenario": "您編輯了一份包含多個章節的課程計畫手冊，希望開啟文件者能透過最上方的目錄快速點選跳轉。",
        "steps": ["選取文件中的章節標題，在工具列將段落樣式套用為「標題 1 (Heading 1)」。", "移至文件開頭，點選選單「插入 -> 目錄 (Table of Contents)」。"],
        "val": "目錄自動抓取「標題 1」文字並生成點選跳轉連結。"
    },
    {
        "num": "04", "key": "Task 04", "tool": "Google Docs (語音擴充外掛)", "title": "國文作文範本非同步親切語音講評", "kw": "語音 註解 外掛 Marketplace Docs Mote",
        "scenario": "批改學生作文時，除了打字外，您希望錄製一段親切的口頭語音，給予學生非同步的聽覺建議。",
        "steps": ["點選選單「擴充功能 -> 外掛程式 -> 取得外掛程式」。", "搜尋安裝 Mote 語音擴充工具。", "在文章段落新增批註，點選錄音發布語音註解。"],
        "val": "註解區出現可直接點擊播放的語音音訊波形。"
    },
    {
        "num": "05", "key": "Task 05", "tool": "Google Docs (翻譯文件)", "title": "新住民家長通知單一鍵雙語翻譯", "kw": "翻譯 多語言 雙語 Docs 通訊 家長",
        "scenario": "班上有新住民家長，您需要將中文的每週班級通訊快速轉換為越南語版本。",
        "steps": ["開啟中文通訊文件，點選頂部選單「工具 -> 翻譯文件」。", "選擇目標語言「越南語」，點選「翻譯」。"],
        "val": "系統自動產生並開啟一份完整的越南語翻譯新文件。"
    },
    {
        "num": "06", "key": "Task 06", "tool": "Google Calendar (預約時間表)", "title": "教師自主學習諮詢預約系統", "kw": "預約時間表 Calendar 親師面談 時間區塊 網址",
        "scenario": "您每週開放 2 小時提供學生課後諮詢，需要讓學生自主預約且不發生時間衝突。",
        "steps": ["在 Calendar 點選「建立 -> 預約時間表」。", "設定單次諮詢時段為 20 分鐘與每週開放時間。", "儲存後複製公開預約網址 (URL) 發送給學生。"],
        "val": "學生點擊網址即可看見剩餘空閒時段並進行預約。"
    },
    {
        "num": "07", "key": "Task 07", "tool": "Google Meet (視訊與串流直播)", "title": "跨校讀書會大型研討與直播開啟", "kw": "Meet 直播 Live Stream 視訊 跨校",
        "scenario": "舉辦跨校線上講座，除了邀請主講者外，還需要開放全校數百名師生線上觀看直播。",
        "steps": ["在 Calendar 建立研討會活動，點選「新增 Google Meet 視訊會議」。", "點選 Meet 視訊選單下拉，點選「新增串流直播 (Add live stream)」。"],
        "val": "活動中生成 Meet 視訊網址與觀看直播網址。"
    },
    {
        "num": "08", "key": "Task 08", "tool": "Google Calendar (與會者權限)", "title": "大型研討會與會者隱私權限防護", "kw": "Calendar 權限 隱私 Email 提醒 通知",
        "scenario": "邀請外部專家開會，需設定 1 小時前 Email 提醒，並禁止受邀者自行邀請他人或查看完整名單。",
        "steps": ["在活動設定中新增通知選取「Email」，時間設為「1 小時前」。", "在與會者權限中，取消勾選「邀請他人」與「檢視與會者名單」。"],
        "val": "與會同仁無法複製或洩漏其他與會者的個資。"
    },
    {
        "num": "09", "key": "Task 09", "tool": "Google Calendar & Docs (會議紀錄)", "title": "學期教研會會議紀錄一鍵同步分發", "kw": "Calendar Docs 會議紀錄 Meeting Notes 共筆",
        "scenario": "教研會開會時，需要讓所有出席者同時開啟同一份會議紀錄文件進行共筆。",
        "steps": ["在日曆活動編輯視窗中，點選「新增會議紀錄 (Add meeting notes)」。"],
        "val": "系統自動建立連動的 Docs，並將閱讀/編輯權限自動賦予所有與會者。"
    },
    {
        "num": "10", "key": "Task 10", "tool": "Google Classroom (協同教師)", "title": "跨校雙語協同教學班級建置", "kw": "Classroom 協同教師 Co-teachers 邀請 共同授課",
        "scenario": "您與另一位外籍教師共同授課，需要給予外師管理作業與批改成績的完整權限。",
        "steps": ["進入 Classroom「成員」頁面。", "在教師區塊點選「邀請教師」，輸入外師 Email 加入為 Co-teacher。"],
        "val": "外師接受後即可共同發布作業與批改成績。"
    },
    {
        "num": "11", "key": "Task 11", "tool": "Google Classroom (成績匯入)", "title": "線上形成性評量分數一鍵同步成績冊", "kw": "Classroom 測驗作業 Grade Importing 成績匯入 Forms",
        "scenario": "在 Classroom 發布 Google 表單測驗，希望學生完成後分數能自動帶入 Classroom 成績冊。",
        "steps": ["點選「建立 -> 測驗作業 (Quiz Assignment)」。", "確認右側「成績匯入 (Grade importing)」切換開關已開啟。"],
        "val": "學生完成 Forms 測驗後，分數旁邊出現「匯入成績」按鈕。"
    },
    {
        "num": "12", "key": "Task 12", "tool": "Google Classroom (原創性比對)", "title": "高中社會科小論文抄襲自主檢查", "kw": "Classroom 原創性比對 Originality Reports 抄襲 檢查",
        "scenario": "要求學生繳交小論文，希望學生在正式提交前能自己檢查是否有無意間抄襲。",
        "steps": ["建立作業時，在右側側邊欄勾選「檢查原創性 (Originality reports)」。"],
        "val": "學生端提交作業前可免費進行最多 3 次全網抄襲比對。"
    },
    {
        "num": "13", "key": "Task 13", "tool": "Google Slides (投影片超連結)", "title": "英檢單字互動記憶卡製作", "kw": "Slides 超連結 記憶卡 Hyperlink 選擇板 頁面跳轉",
        "scenario": "製作單字複習簡報，點選單字按鈕後能自動跳轉至顯示解答的特定投影片頁面。",
        "steps": ["選取簡報上的單字按鈕，按右鍵選取「連結」。", "選擇「簡報中的投影片 (Slides in this presentation)」，選取目標解答頁碼。"],
        "val": "簡報播放時點擊按鈕直接跳轉至解答頁。"
    },
    {
        "num": "14", "key": "Task 14", "tool": "Google Slides (主題建構工具)", "title": "全校統一簡報母版與圖片預留框", "kw": "Slides 主題建構工具 Theme Builder 預留位置 Placeholder",
        "scenario": "為學校團隊製作標準報告簡報，設置統一格式的圖片上傳預留框。",
        "steps": ["點選選單「檢視 -> 主題建構工具」。", "點選「插入 -> 預留位置 -> 圖片預留位置 (Image placeholder)」。"],
        "val": "回到主頁面時出現一鍵點擊上傳圖片的預留框。"
    },
    {
        "num": "15", "key": "Task 15", "tool": "Google Slides (影片內嵌與指派)", "title": "簡報內嵌入 YouTube 實驗影片與批註指派", "kw": "Slides 影片 內嵌 YouTube 註解 指派 Assign",
        "scenario": "在簡報內直接播放教學影片，並標記同仁進行發布前的影片審閱。",
        "steps": ["點選「插入 -> 影片」搜尋內嵌 YouTube 影片。", "選取影片新增註解，輸入 +成員Email 並勾選「指派給...」。"],
        "val": "影片可在簡報內播放，同仁收到指派 Email。"
    },
    {
        "num": "16", "key": "Task 16", "tool": "Google Sites (子頁面 Subpages)", "title": "班級自然科學小組專題展示網站", "kw": "Sites 子頁面 Subpages PBL 專題 展示 頁面",
        "scenario": "為 PBL 專題建立網站，並為每個小組設定獨立的專屬展演分頁。",
        "steps": ["進入 Google Sites 右側點選「頁面 (Pages)」。", "點選底部「+」選擇「新增子頁面 (Subpage)」，輸入「第一組」。"],
        "val": "頂部導覽列出現下拉式的子頁面選單。"
    },
    {
        "num": "17", "key": "Task 17", "tool": "Google Sites & Docs (發布權限)", "title": "高中生學習歷程檔案公開大學審閱", "kw": "Sites Docs 發布 權限 Public 發布至網路 大學審閱",
        "scenario": "學生的 Sites 網站要開放給外部大學評審觀看，且內嵌的 Docs 不能顯示「無權限」。",
        "steps": ["點選 Sites 右上角「發布」，管理權限設為「公開 (Public)」。", "開啟內嵌的 Docs 文件，點選「檔案 -> 發布至網路」。"],
        "val": "任何未登入的外部評審皆能順暢瀏覽網站與文件。"
    },
    {
        "num": "18", "key": "Task 18", "tool": "Google Sheets (條件式格式)", "title": "期中測驗不及格警示自動化", "kw": "Sheets 條件式格式 Conditional Formatting 不及格 紅底白字",
        "scenario": "在成績單中，讓分數低於 60 分的儲存格自動呈現醒目的紅底白字。",
        "steps": ["選取成績欄位，點選選單「格式 -> 條件式格式設定」。", "條件選「小於 60」，樣式設為紅底白字。"],
        "val": "所有不及格分數即時自動變紅。"
    },
    {
        "num": "19", "key": "Task 19", "tool": "Google Sheets (直行統計與樞紐)", "title": "運動會進場服裝投票統計與樞紐分析", "kw": "Sheets 直行統計 Column Stats 樞紐分析表 Pivot Table 投票",
        "scenario": "收集了數百筆表單回應，需要快速統計每個服裝顏色的精確票數。",
        "steps": ["選取顏色欄位，點選選單「資料 -> 直行統計」看圖表。", "點選「插入 -> 樞紐分析表」，拉入顏色與計數。"],
        "val": "一秒自動生成顏色投票總計表格。"
    },
    {
        "num": "20", "key": "Task 20", "tool": "Google Meet (電話撥號加入)", "title": "山區戶外觀察即時語音會議連線", "kw": "Meet 電話撥號 Join by Phone 網路不穩 音訊",
        "scenario": "戶外考察時網路訊號極差，老師需要透過電話撥號收聽線上會議。",
        "steps": ["在 Meet 點選下方「三點圖示 -> 使用電話收聽及發言」。", "依提示用手機撥打電話號碼並輸入 PIN 碼。"],
        "val": "透過行動電話網路穩定參與音訊會議。"
    },
    {
        "num": "21", "key": "Task 21", "tool": "Practice Sets (額外協助提示)", "title": "國中理化自主複習題組影音腳手架", "kw": "Practice Sets 額外協助 Extra Help 提示 影片 腳手架",
        "scenario": "在題目下方加入解題提示影音，讓答錯的學生獲得及時輔導。",
        "steps": ["建立 Practice Sets，在題目下方點選「額外協助 (Extra help)」。", "點選「+ 新增資源」搜尋內嵌 YouTube 輔導影片。"],
        "val": "學生答題卡關時可點擊播放解題影片。"
    },
    {
        "num": "22", "key": "Task 22", "tool": "Practice Sets (題組共用連結)", "title": "同科備課團隊共享自製練習題組", "kw": "Practice Sets 共用連結 Link Sharing 備課 共享",
        "scenario": "製作好 Practice Sets 題組後，將連結共享給同科夥伴直接複製使用。",
        "steps": ["點選右上角「分享」，點選「開啟連結共用」。", "複製連結發送給團隊夥伴。"],
        "val": "夥伴點擊連結即可複製題組至其 Classroom。"
    },
    {
        "num": "23", "key": "Task 23", "tool": "Google Forms (區段跳轉)", "title": "翻轉課堂先備知識檢測與分流教學", "kw": "Forms 區段跳轉 依回應跳轉 翻轉課堂 適性化",
        "scenario": "表單內播放影片後提問，答對者跳轉進階區段，答錯者跳轉補救區段。",
        "steps": ["點選單選題右下角三點圖示，勾選「依據回應跳轉至不同區段」。", "在各選項指定對應跳轉之區段。"],
        "val": "填答者依據選擇走向不同的學習分流。"
    },
    {
        "num": "24", "key": "Task 24", "tool": "Gmail (帳戶代理授權)", "title": "行政科室公用信箱代理收發授權", "kw": "Gmail 代理 帳戶授權 Grant Access 收發 信箱",
        "scenario": "主管需要授權秘書代表自己發送公文郵件，且不透露密碼。",
        "steps": ["進入 Gmail 右上角「設定 -> 查看所有設定 -> 帳戶與匯入」。", "在「授予您帳戶的存取權」點選新增代理 Email。"],
        "val": "秘書可在其 Gmail 中切換並代表主管發信。"
    },
    {
        "num": "25", "key": "Task 25", "tool": "Google Docs & Meet (檔案內Meet)", "title": "文件內即時視訊邊看邊修範本", "kw": "Docs Meet 檔案內 視訊邊看邊修 協作",
        "scenario": "共同編輯 Docs 文件時，希望直接在文件右上角發起 Meet 視訊邊討論邊修改。",
        "steps": ["在 Docs 右上角點選 Meet 視訊圖示。", "點選「在此發起新會議」並分享畫面。"],
        "val": "視訊畫面浮動於文件右側，實現實態檔案內協作。"
    }
]

# Generate cards HTML for hands_on_tasks_app.html
cards_html = ""
for t in tasks_data:
    key = t["key"]
    info = links_data.get(key, {})
    url = info.get("url", "#")
    t_type = info.get("type", "Docs")
    
    steps_list = ""
    for idx, s in enumerate(t["steps"], 1):
        steps_list += f'<div class="step-item"><input type="checkbox" id="{key}-s{idx}"><label for="{key}-s{idx}">{s}</label></div>\n'

    cards_html += f'''
      <!-- {key} -->
      <div class="task-card" data-keywords="{t["kw"]}">
        <div class="task-header">
          <span class="task-num">實務演練 {t["num"]}</span>
          <span class="tool-badge">{t["tool"]}</span>
        </div>
        <h2 class="task-title">{t["title"]}</h2>
        
        <div style="background:#e6f4ea; border:1px solid #34a853; border-radius:8px; padding:12px 16px; margin:12px 0; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <div>
            <strong style="color:#137333;">🔗 本題雲端真實線上 {t_type} 實作檔案：</strong>
            <span style="font-size:0.85rem; color:#5f6368; display:block;">（點擊開啟實檔即可直接在畫面上進行功能實操演練！）</span>
          </div>
          <a href="{url}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:8px 16px; border-radius:18px; font-weight:700; font-size:0.88rem; box-shadow:0 2px 4px rgba(0,0,0,0.1);">📄 開啟線上 {t_type} 實作檔</a>
        </div>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：{t["scenario"]}
        </div>
        <h3>▶️ 上機手把手修改演練步驟：</h3>
        <div class="step-list">
          {steps_list}
        </div>
        <div class="validation">✨ 成果驗證點：{t["val"]}</div>
      </div>
'''

# Update hands_on_tasks_app.html
app_template = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>25 個全實作原創教學情境演練 App (附雲端真實檔案)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --primary-light: #e8f0fe;
      --text-main: #202124;
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

    .container {{
      max-width: 1100px;
      margin: 28px auto;
      padding: 0 20px;
    }}

    .search-box {{
      margin-bottom: 24px;
      display: flex;
      gap: 12px;
    }}

    .search-input {{
      flex: 1;
      padding: 12px 18px;
      border-radius: 24px;
      border: 1px solid var(--border);
      font-size: 0.95rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      outline: none;
    }}

    .search-input:focus {{ border-color: var(--primary); }}

    .task-card {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: var(--shadow);
      border-left: 5px solid var(--primary);
    }}

    .task-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .task-num {{
      font-size: 0.82rem;
      font-weight: 700;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 10px;
      border-radius: 12px;
    }}

    .task-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--primary-dark);
    }}

    .scenario-box {{
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 14px 16px;
      border-radius: 0 8px 8px 0;
      margin: 14px 0;
      font-size: 0.93rem;
    }}

    .scenario-box strong {{ color: #b06000; }}

    .tool-badge {{
      display: inline-block;
      background: #e6f4ea;
      color: #137333;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}

    .step-list {{
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      margin: 14px 0;
    }}

    .step-item {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      margin-bottom: 10px;
      font-size: 0.92rem;
    }}

    .step-item input[type="checkbox"] {{
      margin-top: 4px;
      width: 18px;
      height: 18px;
      cursor: pointer;
    }}

    .validation {{
      background: #e8f0fe;
      color: #1967d2;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>🛠️ 25 個全實作原創教學情境演練 App</h1>
      <p>無考題痕跡 ‧ 工具功能導向 ‧ 附 25 個雲端真實 Google 實作檔網址</p>
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
      {cards_html}
    </div>
  </div>

  <script>
    function filterTasks() {{
      const q = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.task-card');
      cards.forEach(card => {{
        const kw = card.getAttribute('data-keywords').toLowerCase();
        const text = card.innerText.toLowerCase();
        if (!q || kw.includes(q) || text.includes(q)) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
'''

path_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_app, 'w', encoding='utf-8') as f:
    f.write(app_template)

print("Successfully updated hands_on_tasks_app.html with ALL 25 REAL LINKS!")
