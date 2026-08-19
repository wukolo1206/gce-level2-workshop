# -*- coding: utf-8 -*-
"""
產生「講師版覆蓋對照表」instructor_coverage_map.html。

用途：確認 25 題選擇題 + 3 個實作題（15 個 Task）的每一個考點，
都有對應的工具章節演練，且標明各功能的帳號授權門檻。

⚠️ 這一頁是給講師備課用的，刻意不從任何學員端 App 連過去——
學員端維持「情境 ➔ 功能 ➔ 實作」的自然結構，看不到考題編號。
"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

G_OK = ('', '#137333')                      # 一般帳號可做
G_FUND = ('需學校 Education 帳號', '#b06000')  # Fundamentals 以上
G_PLUS = ('需 Education Plus / T&L', '#b3261e')
G_WS = ('需 Workspace（個人 Gmail 多半無）', '#b06000')

# 25 題選擇題 → 章節演練
QUIZ = [
    ('Q01', '系列活動排程＋附加 Meet', 'Calendar 演練二＋演練五', G_OK),
    ('Q02', 'Sites 為每位學生建子頁面', 'Sites 演練一', G_OK),
    ('Q03', 'Marketplace 外掛做語音回饋', 'Docs 演練五', G_OK),
    ('Q04', '智慧型畫布 @People @Date', 'Docs 演練一', G_OK),
    ('Q05', 'Meet 透過電話加入', 'Meet 演練一', G_WS),
    ('Q06', '段落樣式建立文件結構', 'Docs 演練二', G_OK),
    ('Q07', 'Classroom 原創性比對報告', 'Classroom 演練四', G_FUND),
    ('Q08', 'Practice Sets 額外協助（10 個資源）', 'Practice Sets 演練一', G_PLUS),
    ('Q09', 'Sheets 條件式格式視覺化', 'Sheets 演練一', G_OK),
    ('Q10', 'Calendar 預約時間表', 'Calendar 演練一', G_OK),
    ('Q11', 'Sites 發布設定', 'Sites 演練二', G_OK),
    ('Q12', 'Docs 尋找與取代', 'Docs 演練三', G_OK),
    ('Q13', '表格＋超連結探索清單／翻轉課堂表單（複選）', 'Docs 演練七＋Forms 演練一', G_OK),
    ('Q14', '會議記錄文件附加至日曆邀請', 'Calendar 演練四', G_OK),
    ('Q15', '直行統計＋樞紐分析（複選）', 'Sheets 演練二', G_OK),
    ('Q16', 'Classroom 建班並加協同教師', 'Classroom 演練一', G_OK),
    ('Q17', '測驗作業＋成績匯入', 'Classroom 演練三＋Forms 演練二', G_OK),
    ('Q18', 'Slides 兩種建立連結路徑（複選）', 'Slides 演練一', G_OK),
    ('Q19', 'Practice Sets 開啟連結共用', 'Practice Sets 演練二', G_PLUS),
    ('Q20', 'Docs 翻譯文件', 'Docs 演練四', G_OK),
    ('Q21', 'Slides 內嵌 YouTube 影片', 'Slides 演練三', G_OK),
    ('Q22', 'Gmail 授予帳戶存取權（代理）', 'Gmail 演練一', G_OK),
    ('Q23', 'Sites 公開＋文件發布至網路', 'Sites 演練二', G_OK),
    ('Q24', '從 Docs／Slides 檔案內發起 Meet（複選）', 'Meet 演練二', G_OK),
    ('Q25', 'Slides 超連結製作記憶卡', 'Slides 演練一', G_OK),
]

# 3 個實作題（15 Task）→ 章節演練
LABS = [
    ('Lab 1 Classroom', 'T1 建立班級', 'Classroom 演練一', G_OK),
    ('Lab 1 Classroom', 'T2 邀請協同教師與學生', 'Classroom 演練一', G_OK),
    ('Lab 1 Classroom', 'T3 建立兩個主題', 'Classroom 演練二', G_OK),
    ('Lab 1 Classroom', 'T4 建立作業與素材（檔案權限）', 'Classroom 演練二', G_OK),
    ('Lab 1 Classroom', 'T5 發布班級公告', 'Classroom 演練五', G_OK),
    ('Lab 2 Calendar', 'T1 建立活動並夾帶檔案', 'Calendar 演練五', G_OK),
    ('Lab 2 Calendar', 'T2 設定 Meet 串流直播', 'Calendar 演練二', G_PLUS),
    ('Lab 2 Calendar', 'T3 新增活動地點', 'Calendar 演練五', G_OK),
    ('Lab 2 Calendar', 'T4 設定 Email 提醒', 'Calendar 演練三', G_OK),
    ('Lab 2 Calendar', 'T5 邀請與會者並限制權限', 'Calendar 演練三', G_OK),
    ('Lab 3 Slides', 'T1 建立簡報與標題頁', 'Slides 演練二', G_OK),
    ('Lab 3 Slides', 'T2 母版與圖片預留位置（須精確命名）', 'Slides 演練二', G_OK),
    ('Lab 3 Slides', 'T3 批註指派投影片', 'Slides 演練三', G_OK),
    ('Lab 3 Slides', 'T4 內嵌 Drive 影片', 'Slides 演練三', G_OK),
    ('Lab 3 Slides', 'T5 分享給主管設註解者權限', 'Slides 演練四', G_OK),
]

# 帳號能力對照
MATRIX = [
    ('Docs / Sheets / Slides / Forms 全部功能', '✅', '✅', '✅'),
    ('Sites 建站與發布', '✅', '✅', '✅'),
    ('Gmail 帳戶代理（授予存取權）', '✅', '✅', '✅'),
    ('Calendar 預約時間表', '✅', '✅', '✅'),
    ('Calendar 建立會議記錄', '✅', '✅', '✅'),
    ('Classroom 建課與協同教師', '✅', '✅', '✅'),
    ('Classroom 原創性比對報告', '❌', '✅（有數量上限）', '✅ 無上限'),
    ('Meet 主持人控制項', '✅', '✅', '✅'),
    ('Meet 分組討論室（當主持人）', '❌', '✅', '✅'),
    ('Meet 電話撥號加入', '❌ 台灣多半無', '✅', '✅'),
    ('Meet 串流直播 (Live stream)', '❌ 只有齒輪，無展開箭頭', '❌ 有箭頭但只給會議代碼', '✅'),
    ('Practice Sets', '❌', '❌', '✅'),
]


def rows_quiz():
    out = ''
    for qid, topic, where, gate in QUIZ:
        txt, color = gate
        badge = (f'<span style="color:{color}; font-weight:700; font-size:0.85rem;">{txt}</span>'
                 if txt else '<span style="color:#137333;">一般帳號可做</span>')
        out += (f'<tr><td style="font-weight:700; color:#1a73e8;">{qid}</td>'
                f'<td>{topic}</td><td style="font-weight:600;">{where}</td><td>{badge}</td></tr>')
    return out


def rows_lab():
    out = ''
    prev = ''
    for lab, task, where, gate in LABS:
        txt, color = gate
        badge = (f'<span style="color:{color}; font-weight:700; font-size:0.85rem;">{txt}</span>'
                 if txt else '<span style="color:#137333;">一般帳號可做</span>')
        cell = lab if lab != prev else ''
        prev = lab
        out += (f'<tr><td style="font-weight:700; color:#7b1fa2;">{cell}</td>'
                f'<td>{task}</td><td style="font-weight:600;">{where}</td><td>{badge}</td></tr>')
    return out


def rows_matrix():
    out = ''
    for feat, a, b, c in MATRIX:
        def cell(v):
            col = '#137333' if v.startswith('✅') else '#b3261e'
            return f'<td style="color:{col}; font-weight:700;">{v}</td>'
        out += f'<tr><td style="text-align:left;">{feat}</td>{cell(a)}{cell(b)}{cell(c)}</tr>'
    return out


HTML = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>【講師版】考點覆蓋對照表</title>
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Noto Sans TC',sans-serif; background:#f8f9fa; color:#202124; line-height:1.6; padding:32px 20px; }}
  .wrap {{ max-width:1100px; margin:0 auto; }}
  header {{ background:#5f6368; color:white; padding:24px 28px; border-radius:12px; margin-bottom:24px; }}
  h1 {{ font-size:1.5rem; }}
  header p {{ opacity:.9; font-size:.92rem; margin-top:6px; }}
  h2 {{ font-size:1.2rem; color:#1557b0; margin:28px 0 12px; }}
  table {{ width:100%; border-collapse:collapse; background:white; border-radius:10px;
           overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,.06); font-size:.92rem; }}
  th {{ background:#e8f0fe; color:#1557b0; padding:12px; text-align:left; font-size:.88rem; }}
  td {{ padding:11px 12px; border-top:1px solid #e8eaed; vertical-align:top; }}
  tr:hover td {{ background:#f8f9fa; }}
  .note {{ background:#fff8e1; border-left:4px solid #f9ab00; padding:16px 20px;
           border-radius:0 8px 8px 0; margin:20px 0; }}
  .matrix td:not(:first-child), .matrix th:not(:first-child) {{ text-align:center; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>🎓【講師版】考點覆蓋對照表</h1>
    <p>25 題選擇題 ＋ 3 個實作題（15 Task）＝ 全部對應到工具章節的 40 個演練。學員端不顯示任何考題編號。</p>
  </header>

  <h2>🧰 講師專用工具（學員端已移除）</h2>
  <div style="display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:14px; margin-bottom:8px;">
    <a href="quiz_app.html" style="display:block; text-decoration:none; background:#e6f4ea; border:1px solid #a8dab5;
       border-radius:10px; padding:16px;">
      <strong style="color:#137333; font-size:1rem;">📝 25 題刷題 App（A／B 卷）</strong>
      <div style="color:#5f6368; font-size:.86rem; margin-top:5px;">官方真題雙語對照，可切繁中／English／中英對照。研習尾聲帶學員實戰用。</div></a>
    <a href="hands_on_tasks_app.html" style="display:block; text-decoration:none; background:#fef7e0; border:1px solid #fde293;
       border-radius:10px; padding:16px;">
      <strong style="color:#b06000; font-size:1rem;">🛠️ 25 個實作演練 App</strong>
      <div style="color:#5f6368; font-size:.86rem; margin-top:5px;">與工具講義同一批任務的另一種排列（依 Task 編號），備課核對進度用。</div></a>
    <a href="lab_exercises_app.html" style="display:block; text-decoration:none; background:#e0f2f1; border:1px solid #80cbc4;
       border-radius:10px; padding:16px;">
      <strong style="color:#00695c; font-size:1rem;">🎯 3 個官方實作題 Lab</strong>
      <div style="color:#5f6368; font-size:.86rem; margin-top:5px;">Lab 1 Classroom／Lab 2 Calendar／Lab 3 Slides 的完整 Task 拆解與自動評分注意事項。</div></a>
  </div>
  <p style="color:#5f6368; font-size:.88rem; margin-bottom:20px;">
    這三個都是<strong>備考導向</strong>的工具，已從學員端側邊欄移除，避免研習變成考古題班；
    需要時由講師自行開啟或現場公布網址即可。</p>

  <div class="note">
    <strong>使用方式</strong>：這一頁只給講師備課核對用，<strong>刻意沒有從任何學員端 App 連過來</strong>。
    學員看到的是「實務情境 ➔ 功能說明 ➔ 動手實作」，不會察覺是在對考題。
    帶研習時若時間不足，可優先確保<strong>一般帳號做得到</strong>的項目全部走過一遍，
    授權受限的三項（串流直播、Practice Sets、原創性比對）改以示範帶過即可。
  </div>

  <h2>📝 25 題選擇題覆蓋對照</h2>
  <table>
    <tr><th style="width:70px;">題號</th><th>考點</th><th style="width:230px;">對應章節演練</th><th style="width:220px;">帳號門檻</th></tr>
    {rows_quiz()}
  </table>

  <h2>🛠️ 3 個實作題（Lab Exams）覆蓋對照</h2>
  <table>
    <tr><th style="width:140px;">實作題</th><th>Task</th><th style="width:180px;">對應章節演練</th><th style="width:220px;">帳號門檻</th></tr>
    {rows_lab()}
  </table>

  <h2>🔑 帳號能力對照表</h2>
  <table class="matrix">
    <tr><th>功能</th><th style="width:200px;">個人 Gmail</th><th style="width:210px;">Education Fundamentals</th><th style="width:170px;">Education Plus / T&amp;L</th></tr>
    {rows_matrix()}
  </table>

  <div class="note" style="margin-top:24px;">
    <strong>⚠️ 報考前務必提醒學員</strong>：官方 <strong>Lab 2 的 Task 2 直接要求設定 Meet 串流直播</strong>，
    而該功能需 Education Plus 或 Teaching and Learning Upgrade。
    用個人 Gmail 或學校 Fundamentals 帳號應考，這一項會做不出來——請務必確認應考帳號的授權等級。
  </div>
</div>
</body>
</html>
'''

with io.open(os.path.join(ROOT, 'instructor_coverage_map.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print('instructor_coverage_map.html 已產生：25 題 +', len(LABS), '個 Lab Task +', len(MATRIX), '項帳號能力對照')
