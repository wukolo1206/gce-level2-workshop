import json, os, re

root = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

instructions = {
    "Task 01": "請按下快捷鍵 Ctrl + H 開啟「尋找與取代」，將文件中所有的舊校長姓名「陳大文」，一次性全部取代更正為新校長姓名「張小明」！",
    "Task 02": "請在文件中的「負責人」欄位輸入 @ 插入 @People 人員晶片；在「完成期限」欄位輸入 @ 插入 @Date 日期晶片！",
    "Task 03": "請選取文件中的「第一章、第二章、第三章」章節標題套用「標題 1」段落樣式，並在頂部點選「插入 ➔ 頁面元素 ➔ 目錄」！",
    "Task 04": "請點選選單「擴充功能 ➔ 外掛程式 ➔ 取得外掛程式」安裝 Mote 外掛，並在本作文段落新增註解錄製一段語音回饋！",
    "Task 05": "請點選選單「工具 ➔ 翻譯文件」，選擇目標語言（如越南語或印尼語），自動生成一份完整的雙語翻譯新文件！",
    "Task 06": "請在 Google Calendar 點選「建立 ➔ 預約時間表」，設定親師面談諮詢時段，並複製公開網址發送！",
    "Task 07": "請在日曆活動中新增 Google Meet 視訊，點選選單下拉開啟「新增串流直播 (Add live stream)」！",
    "Task 08": "請在日曆活動設定中新增 1 小時前 Email 提醒，並在與會者權限中取消勾選「邀請他人」與「檢視與會者名單」！",
    "Task 09": "請選取文件段落新增註解，輸入 +成員Email 並勾選「指派給...」核取方塊，交付團隊成員執行！",
    "Task 10": "請進入 Classroom「成員」頁面，在教師區塊點選「邀請教師」，輸入夥伴 Email 加入為「協同教師 (Co-teachers)」！",
    "Task 11": "請建立「測驗作業 (Quiz Assignment)」，確認右側控制面板中的「成績匯入 (Grade importing)」切換開關已開啟！",
    "Task 12": "請在作業編輯面板下方，勾選「檢查原創性 (Originality reports)」小方塊！",
    "Task 13": "請選取簡報上的單字按鈕按右鍵選「連結」，選擇「簡報中的投影片 (Slides in this presentation)」設定跳轉答案頁！",
    "Task 14": "請點選選單「檢視 ➔ 主題建構工具」，點選「插入 ➔ 預留位置 ➔ 圖片預留位置」設計母版！",
    "Task 15": "請點選「插入 ➔ 影片」內嵌 YouTube 影音，並選取影片新增註解輸入 +成員Email 勾選「指派給...」！",
    "Task 16": "請進入 Google Sites 右側點選「頁面 ➔ + ➔ 新增子頁面 (Subpage)」，為小組建立專屬 Showcase 頁面！",
    "Task 17": "請點選 Sites 右上角「發布」設為「公開 (Public)」，並將內嵌的 Docs 點選「檔案 ➔ 發布至網路」！",
    "Task 18": "請選取分數欄位，點選選單「格式 ➔ 條件式格式設定」，將小於 60 分的儲存格設定為紅底白字醒目提示！",
    "Task 19": "請選取顏色欄位點選「資料 ➔ 直行統計」看圖表；並點選「插入 ➔ 樞紐分析表」統計各顏色總票數！",
    "Task 20": "請在 Meet 控制列下方點選「三點圖示 ➔ 使用電話收聽及發言」，輸入 PIN 碼透過電話語音參與！",
    "Task 21": "請在 Practice Sets 題目下方點選「額外協助 (Extra help)」，加入 YouTube 教學影片或文字提示卡！",
    "Task 22": "請點選 Practice Sets 右上角「分享」，點選「開啟連結共用」，複製連結分享給同備課團隊！",
    "Task 23": "請點選 Forms 單選題右下角三點圖示，勾選「依據回應跳轉至不同區段」，並指定各選項對應之區段！",
    "Task 24": "請進入 Gmail 右上角「設定 ➔ 查看所有設定 ➔ 帳戶與匯入」，在「授予您帳戶的存取權」點選新增代理 Email！",
    "Task 25": "請在 Docs 右上角點選 Meet 視訊圖示，點選「在此發起新會議」，邊看文件邊線上討論修訂！"
}

links_path = os.path.join(root, 'all_25_real_workspace_links.json')
with open(links_path, 'r', encoding='utf-8') as f:
    links = json.load(f)

def make_detailed_box(t_key, file_type, title):
    url = links.get(t_key, {}).get('url', '#')
    inst = instructions.get(t_key, "請點選開啟實做檔並依照步驟完成設定！")
    
    return f'''
        <div style="background:#e6f4ea; border:2px solid #34a853; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#137333; font-size:1.05rem; display:flex; align-items:center; gap:6px;">
              🔗 本單元線上真實 {file_type} 實作檔案：
            </strong>
            <a href="{url}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:10px 22px; border-radius:20px; font-weight:700; font-size:0.92rem; box-shadow:0 3px 8px rgba(0,0,0,0.15); transition:all 0.2s;">📄 點此開啟真實 {file_type} 實作檔</a>
          </div>
          <div style="background:white; border:1px solid #a8dab5; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.88rem; color:#5f6368; margin-bottom:4px;">檔名：<strong>{title}</strong></div>
            <div style="font-size:0.95rem; color:#137333; font-weight:700; line-height:1.5;">
              🎯 本檔具體修改任務：<span style="color:#202124; font-weight:500;">{inst}</span>
            </div>
          </div>
        </div>
'''

# Update docs_workshop_app.html
p_docs = os.path.join(root, 'docs_workshop_app.html')
docs_map = [
    ("Task 02", "智慧型畫布 (Smart Canvas) 與團隊任務指派"),
    ("Task 03", "結構化排版與動態導覽目錄 (Paragraph Styles)"),
    ("Task 01", "高效內文檢索與批次修正 (Find and Replace)"),
    ("Task 05", "跨語言親師溝通與文件一鍵翻譯 (Translate Document)"),
    ("Task 04", "非同步語音註解與多媒體回饋 (Marketplace Add-ons)"),
    ("Task 09", "跨軟體行政整合 (行事曆與簡報批註連動)")
]

with open(p_docs, 'r', encoding='utf-8') as f:
    h_docs = f.read()

# Clean up old link boxes
h_docs = re.sub(r'<div style="background:#e6f4ea.*?(?=<h2>|<div class="scenario-box"|<div class="step-list")', '', h_docs, flags=re.DOTALL)

# Re-inject new detailed boxes
for t_key, heading in docs_map:
    t_title = links.get(t_key, {}).get('title', heading)
    new_box = make_detailed_box(t_key, "Google Docs", t_title)
    target_h = f'<h2>{heading}</h2>'
    if target_h in h_docs:
        h_docs = h_docs.replace(target_h, target_h + '\n' + new_box)

with open(p_docs, 'w', encoding='utf-8') as f:
    f.write(h_docs)

print("Updated docs_workshop_app.html with detailed task instructions!")
