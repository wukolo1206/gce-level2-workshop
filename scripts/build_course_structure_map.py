# -*- coding: utf-8 -*-
"""
產生「課程結構三方對照」course_structure_map.html（學員可用版）。

要解決的困惑：Google 官方 Level 2 有<兩套不同的課程結構>——
  ‧ 英文版 Path 1717663：6 大單元 / 18 個 Lessons（考試大綱也是這 6 大領域）
  ‧ 繁中版 Path 1727915：11 個實務教學情境單元
學員從不同語言的官方頁面進來，看到的目錄完全不一樣，很容易以為自己漏學了。

本頁把兩套結構與我們的 10 篇工具講義對起來，
並保留「單元＝綜合應用情境」這條軸線：一個教學情境要串哪幾個工具。
（考題編號只出現在講師版 instructor_coverage_map.html，本頁不顯示。）
"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH_EN = 'https://edu.exceedlms.com/student/path/1717663'
PATH_ZH = 'https://edu.exceedlms.com/student/path/1727915?locale=zh_tw'

# 英文版 6 大單元（＝考試大綱 6 大能力領域）
UNITS6 = {
    1: ('自動化行政任務', 'Automate administrative tasks'),
    2: ('親師與監護人溝通', 'Communicate with guardians'),
    3: ('班級與教學素材', 'Organize class materials'),
    4: ('互動與自主學習', 'Interactive & independent learning'),
    5: ('個人化差異學習', 'Personalize learning'),
    6: ('數據解讀與分析', 'Analyze student data'),
}

TOOL_FILE = {
    'Docs': 'docs_workshop_app.html', 'Calendar': 'calendar_workshop_app.html',
    'Classroom': 'classroom_workshop_app.html', 'Slides': 'slides_workshop_app.html',
    'Sheets': 'sheets_workshop_app.html', 'Meet': 'meet_workshop_app.html',
    'Forms': 'forms_workshop_app.html', 'Sites': 'sites_workshop_app.html',
    'Gmail': 'gmail_workshop_app.html', 'Practice Sets': 'practicesets_workshop_app.html',
}

# 繁中 11 單元 → (主題, 對應英文 Unit, [(工具, 演練)])
UNITS11 = [
    (1, '推廣及示範如何有效運用數位工具', '確立指導程序、引導其他教師、建立與收錄線上學習資源',
     [1, 5], [('Practice Sets', '演練二 題組連結共享'), ('Sites', '演練三 內嵌動態內容')]),
    (2, '善用學習模式建立個人化學習', '打造個人化學習路徑、選擇板、用視覺工具呈現學習成果',
     [5], [('Docs', '演練七 表格＋超連結探索學習單'), ('Forms', '演練一 區段跳轉分流'),
           ('Slides', '演練一 超連結互動記憶卡')]),
    (3, '使用進階功能改善教學流程', '共用日曆、Gmail 代理與篩選器、Marketplace 擴充功能',
     [1], [('Gmail', '演練一 帳戶代理｜演練二 篩選器'), ('Docs', '演練三 尋找與取代｜演練五 語音回饋外掛')]),
    (4, '與監護人交流互動', '彙整監護人資訊、發布全班通知、預約親師面談',
     [2], [('Calendar', '演練一 預約時間表'), ('Docs', '演練四 翻譯文件'),
           ('Gmail', '演練三 範本與排程'), ('Classroom', '演練五 班級公告')]),
    (5, '解析學生資料', '成績快速圖表化、以樞紐分析與條件式格式解讀大型資料集',
     [6], [('Sheets', '演練一 條件式格式｜演練二 樞紐分析'), ('Forms', '演練三 回應驗證與統計')]),
    (6, '有效整理班級和全校教材', '建立課程入口網站、課程大綱目錄與教材結構',
     [3], [('Sites', '演練一 子頁面架構'), ('Docs', '演練二 段落樣式與目錄'),
           ('Classroom', '演練二 主題分頁')]),
    (7, '設計互動式課程', '互動式簡報、內嵌影片、記憶卡與選擇板',
     [4], [('Slides', '演練一 超連結｜演練二 母版｜演練三 內嵌影片')]),
    (8, '走出教室，教學不設限', '跨校與跨國連線、虛擬戶外教學、共同探索環境',
     [2, 4], [('Calendar', '演練二 Meet 與直播｜演練五 系列活動'),
              ('Meet', '演練一 電話撥號備援｜演練三 分組討論室')]),
    (9, '善用 Google 的強大功能進行研究', '進階搜尋策略、翻譯與探索工具、學術誠信',
     [1, 3], [('Classroom', '演練四 原創性比對'), ('Gmail', '演練四 搜尋運算子'),
              ('Docs', '演練四 翻譯文件')]),
    (10, '讓學生暢所欲言', '課堂內外討論、線上發布作品、打造校園生活體驗',
     [3, 5], [('Sites', '演練二 發布權限與公開'), ('Slides', '演練四 分享權限層級'),
              ('Classroom', '演練五 班級公告')]),
    (11, '學生的學習動力與評量', '自主專案、小組領導專案、總評量測驗',
     [5, 6], [('Classroom', '演練三 測驗作業與成績匯入'), ('Forms', '演練二 測驗自動評分'),
              ('Practice Sets', '演練一 額外協助｜演練三 作答洞察')]),
]


def tool_links(tools):
    out = []
    for name, note in tools:
        f = TOOL_FILE[name]
        out.append(f'<div style="margin-bottom:5px;"><a href="{f}" '
                   f'style="color:#1a73e8; font-weight:700; text-decoration:none;">{name}</a>'
                   f'<span style="color:#5f6368; font-size:.87rem;"> ‧ {note}</span></div>')
    return ''.join(out)


def rows11():
    out = ''
    for n, title, topic, u6, tools in UNITS11:
        badges = ''.join(
            f'<span style="display:inline-block; background:#e8f0fe; color:#1557b0; border-radius:10px; '
            f'padding:2px 9px; font-size:.82rem; font-weight:700; margin:0 4px 4px 0;">'
            f'Unit {u} {UNITS6[u][0]}</span>' for u in u6)
        out += (f'<tr>'
                f'<td style="text-align:center; font-weight:700; color:#7b1fa2; white-space:nowrap;">第 {n} 單元</td>'
                f'<td><strong>{title}</strong>'
                f'<div style="color:#5f6368; font-size:.87rem; margin-top:3px;">{topic}</div></td>'
                f'<td>{badges}</td>'
                f'<td>{tool_links(tools)}</td></tr>')
    return out


def rows6():
    out = ''
    for u, (zh, en) in UNITS6.items():
        rel = [f'第 {n} 單元' for n, _, _, u6, _ in UNITS11 if u in u6]
        out += (f'<tr><td style="text-align:center; font-weight:700; color:#1557b0; white-space:nowrap;">Unit {u}</td>'
                f'<td><strong>{zh}</strong><div style="color:#5f6368; font-size:.87rem;">{en}</div></td>'
                f'<td style="color:#7b1fa2; font-weight:600;">{"、".join(rel)}</td></tr>')
    return out


HTML = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>課程結構對照 — 繁中 11 單元 × 英文 6 Units × 工具講義</title>
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Google Sans','Noto Sans TC',sans-serif; background:#f8f9fa; color:#202124; line-height:1.65; }}
  header {{ background:#1a73e8; color:#fff; padding:24px 32px; box-shadow:0 4px 12px rgba(26,115,232,.25);
            display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px; }}
  header h1 {{ font-size:1.45rem; }}
  header p {{ opacity:.92; font-size:.9rem; margin-top:4px; }}
  .nav-btn {{ text-decoration:none; background:rgba(255,255,255,.2); color:#fff; padding:8px 16px;
              border-radius:20px; font-size:.85rem; font-weight:600; }}
  .wrap {{ max-width:1200px; margin:28px auto; padding:0 20px; }}
  .card {{ background:#fff; border-radius:12px; padding:26px; box-shadow:0 4px 16px rgba(0,0,0,.06); margin-bottom:24px; }}
  h2 {{ font-size:1.25rem; color:#1557b0; margin-bottom:14px; }}
  table {{ width:100%; border-collapse:collapse; font-size:.93rem; }}
  th {{ background:#f1f3f4; text-align:left; padding:11px 12px; font-size:.86rem; color:#5f6368; }}
  td {{ padding:13px 12px; border-top:1px solid #e8eaed; vertical-align:top; }}
  tr:hover td {{ background:#fafbfc; }}
  .note {{ background:#fef7e0; border-left:4px solid #f9ab00; padding:16px 20px; border-radius:0 8px 8px 0; margin:18px 0; }}
  .two {{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }}
  @media (max-width:860px) {{ .two {{ grid-template-columns:1fr; }} }}
  .plink {{ display:block; background:#e8f0fe; border-radius:10px; padding:14px 16px; text-decoration:none; color:#1557b0; }}
  .plink strong {{ display:block; font-size:1rem; margin-bottom:3px; }}
  .plink span {{ color:#5f6368; font-size:.85rem; }}
</style>
</head>
<body>
<header>
  <div>
    <h1>🗺️ 課程結構對照：繁中 11 單元 × 英文 6 Units × 工具講義</h1>
    <p>一個教學情境要串哪幾個工具——這是「綜合應用」的視角</p>
  </div>
  <div><a href="study_guide_app.html" class="nav-btn">📖 回研習主講義</a></div>
</header>

<div class="wrap">

  <div class="card">
    <h2>❓ 為什麼官方教材有兩套目錄？</h2>
    <p>很多老師會卡在這裡：打開<strong>英文版</strong>官方課程看到 6 大單元、18 個 Lessons；
       切到<strong>繁體中文版</strong>卻變成 11 個單元，名稱也完全不同，於是懷疑自己是不是漏學了什麼。</p>
    <p style="margin-top:10px;"><strong>兩套教的是同一批內容，只是切法不同：</strong>
       英文版依<strong>能力領域</strong>分（也就是考試大綱的 6 大領域），
       繁中版依<strong>教學情境</strong>分（一個情境通常會跨好幾個工具）。
       兩套都不會漏，選一套走完即可——但知道對應關係，查資料時會快很多。</p>
    <div class="two" style="margin-top:16px;">
      <a class="plink" href="{PATH_EN}" target="_blank">
        <strong>🇬🇧 英文版課程（6 Units / 18 Lessons）</strong>
        <span>Path 1717663 ‧ 考試大綱即依此 6 大領域命題</span></a>
      <a class="plink" href="{PATH_ZH}" target="_blank">
        <strong>🇹🇼 繁體中文版課程（11 個實務單元）</strong>
        <span>Path 1727915 ‧ 依教學情境編排，較貼近現場</span></a>
    </div>
  </div>

  <div class="card">
    <h2>📘 繁中 11 單元 → 對應英文 Unit → 要練哪幾個工具</h2>
    <p style="color:#5f6368; font-size:.9rem; margin-bottom:14px;">
      這張表就是「綜合應用」的地圖：左邊是一個真實教學情境，右邊是達成它需要組合的工具與演練。
      工具名稱可直接點進該篇講義。</p>
    <div style="overflow-x:auto;">
      <table>
        <tr><th style="width:88px;">繁中單元</th><th style="width:32%;">單元主題</th>
            <th style="width:22%;">對應英文 Unit</th><th>要練的工具演練</th></tr>
        {rows11()}
      </table>
    </div>
  </div>

  <div class="card">
    <h2>🔄 反查：英文 6 Units → 散落在哪幾個繁中單元</h2>
    <p style="color:#5f6368; font-size:.9rem; margin-bottom:14px;">
      若你是照<strong>英文版</strong>或<strong>考試大綱</strong>複習的，用這張表回頭找繁中教材的位置。</p>
    <table>
      <tr><th style="width:88px;">英文 Unit</th><th style="width:42%;">能力領域</th><th>對應繁中單元</th></tr>
      {rows6()}
    </table>
    <div class="note" style="margin-top:18px;">
      <strong>💡 兩種視角怎麼用</strong>：想確認自己有沒有能力盲點時，以 <strong>Unit</strong> 為單位逐項檢查；
      實際動手練習時，照<strong>工具篇</strong>走效率最高（同一個工具的功能一次學完，不用在工具之間跳來跳去）。
      兩者不衝突——這張表就是讓你在兩種視角之間自由切換。
    </div>
  </div>

</div>
</body>
</html>
'''

with io.open(os.path.join(ROOT, 'course_structure_map.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('course_structure_map.html 已產生：繁中 11 單元 × 英文 6 Units × 10 篇工具講義三方對照')
