import json, os

links_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\all_25_real_workspace_links.json'
with open(links_path, 'r', encoding='utf-8') as f:
    links = json.load(f)

root = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

def make_link_box(url, file_type, title):
    return f'''
        <div style="background:#e6f4ea; border:1.5px solid #34a853; border-radius:10px; padding:16px; margin:16px 0; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
          <div>
            <strong style="color:#137333; font-size:1.02rem;">🔗 本單元真實線上 {file_type} 實作檔案：</strong>
            <p style="font-size:0.88rem; color:#3c4043; margin-top:4px; margin-bottom:0;">檔名：<strong>{title}</strong>（點擊右側按鈕開啟實檔，即可直接在畫面上進行功能實操演練！）</p>
          </div>
          <a href="{url}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:10px 20px; border-radius:20px; font-weight:700; font-size:0.9rem; box-shadow:0 2px 6px rgba(0,0,0,0.15);">📄 開啟真實 {file_type} 實作檔</a>
        </div>
'''

# 1. Update docs_workshop_app.html
docs_map = [
    ("Task 02", "智慧型畫布 (Smart Canvas) 與團隊任務指派"),
    ("Task 03", "結構化排版與動態導覽目錄 (Paragraph Styles)"),
    ("Task 01", "高效內文檢索與批次修正 (Find and Replace)"),
    ("Task 05", "跨語言親師溝通與文件一鍵翻譯 (Translate Document)"),
    ("Task 04", "非同步語音註解與多媒體回饋 (Marketplace Add-ons)"),
    ("Task 09", "跨軟體行政整合 (行事曆與簡報批註連動)")
]

p_docs = os.path.join(root, 'docs_workshop_app.html')
with open(p_docs, 'r', encoding='utf-8') as f:
    h_docs = f.read()

for t_key, heading in docs_map:
    info = links.get(t_key, {})
    url = info.get('url', '#')
    t_title = info.get('title', heading)
    box = make_link_box(url, "Google Docs", t_title)
    
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_docs and url not in h_docs:
        h_docs = h_docs.replace(target_h, target_h + '\n' + box)

with open(p_docs, 'w', encoding='utf-8') as f:
    f.write(h_docs)
print("Successfully updated docs_workshop_app.html with ALL module links!")

# 2. Update calendar_workshop_app.html
cal_map = [
    ("Task 06", "親師面談預約時間表設定與公開 URL 發布"),
    ("Task 07", "Calendar 活動排定、Google Meet 視訊與串流直播開啟"),
    ("Task 08", "設定活動地點、 Email 通知提醒與精確與會者權限防護")
]
p_cal = os.path.join(root, 'calendar_workshop_app.html')
with open(p_cal, 'r', encoding='utf-8') as f:
    h_cal = f.read()

for t_key, heading in cal_map:
    info = links.get(t_key, {})
    url = info.get('url', '#')
    t_title = info.get('title', heading)
    box = make_link_box(url, "Google Docs/Calendar", t_title)
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_cal and url not in h_cal:
        h_cal = h_cal.replace(target_h, target_h + '\n' + box)

with open(p_cal, 'w', encoding='utf-8') as f:
    f.write(h_cal)
print("Successfully updated calendar_workshop_app.html!")

# 3. Update classroom_workshop_app.html
cls_map = [
    ("Task 10", "建立 Classroom 課程、批次邀請學生與新增協同教師"),
    ("Task 04", "建立主題分頁 (Topics)、一般作業與線上閱讀素材"),
    ("Task 11", "建立測驗作業 (Quiz Assignment) 開啟成績匯入與原創性檢查")
]
p_cls = os.path.join(root, 'classroom_workshop_app.html')
with open(p_cls, 'r', encoding='utf-8') as f:
    h_cls = f.read()

for t_key, heading in cls_map:
    info = links.get(t_key, {})
    url = info.get('url', '#')
    t_title = info.get('title', heading)
    box = make_link_box(url, "Google Docs/Classroom", t_title)
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_cls and url not in h_cls:
        h_cls = h_cls.replace(target_h, target_h + '\n' + box)

with open(p_cls, 'w', encoding='utf-8') as f:
    f.write(h_cls)
print("Successfully updated classroom_workshop_app.html!")

# 4. Update slides_workshop_app.html
sld_map = [
    ("Task 13", "物件與文字超連結 (Hyperlink Slides) 製作單字記憶卡"),
    ("Task 14", "使用主題建構工具 (Theme Builder) 插入圖片預留位置 (Placeholder)"),
    ("Task 15", "簡報內嵌 YouTube 影片與註解 `+Email` 指派審閱任務")
]
p_sld = os.path.join(root, 'slides_workshop_app.html')
with open(p_sld, 'r', encoding='utf-8') as f:
    h_sld = f.read()

for t_key, heading in sld_map:
    info = links.get(t_key, {})
    url = info.get('url', '#')
    t_title = info.get('title', heading)
    box = make_link_box(url, "Google Slides", t_title)
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_sld and url not in h_sld:
        h_sld = h_sld.replace(target_h, target_h + '\n' + box)

with open(p_sld, 'w', encoding='utf-8') as f:
    f.write(h_sld)
print("Successfully updated slides_workshop_app.html!")

# 5. Update sheets_workshop_app.html
sht_map = [
    ("Task 18", "條件式格式設定 (Conditional Formatting) 自動變更儲存格外觀"),
    ("Task 19", "直行統計 (Column stats) 與 樞紐分析表 (Pivot table) 計算回應")
]
p_sht = os.path.join(root, 'sheets_workshop_app.html')
with open(p_sht, 'r', encoding='utf-8') as f:
    h_sht = f.read()

for t_key, heading in sht_map:
    info = links.get(t_key, {})
    url = info.get('url', '#')
    t_title = info.get('title', heading)
    box = make_link_box(url, "Google Sheets", t_title)
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_sht and url not in h_sht:
        h_sht = h_sht.replace(target_h, target_h + '\n' + box)

with open(p_sht, 'w', encoding='utf-8') as f:
    f.write(h_sht)
print("Successfully updated sheets_workshop_app.html!")

print("All tool apps successfully updated with module-level real links!")
