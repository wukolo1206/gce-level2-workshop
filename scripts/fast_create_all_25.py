import os, json, sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = r'd:\備課ai\google workspace\token.json'
creds = Credentials.from_authorized_user_file(token_path)

drive_service = build('drive', 'v3', credentials=creds)
docs_service = build('docs', 'v1', credentials=creds)
sheets_service = build('sheets', 'v4', credentials=creds)
slides_service = build('slides', 'v1', credentials=creds)

def make_public(file_id):
    permission_body = {'role': 'writer', 'type': 'anyone'}
    drive_service.permissions().create(fileId=file_id, body=permission_body).execute()

real_links = {}

# Task 01
real_links["Task 01"] = {
    "title": "全校週報範例 (尋找與取代演練)",
    "type": "Docs",
    "url": "https://docs.google.com/document/d/1kE7fdTcA9Po3xXxpHmt-iaC1EQtKI0QVuEN8HhnQcXE/edit?usp=sharing"
}

# Task 02
doc2 = docs_service.documents().create(body={'title': '運動會籌備會議紀錄 (智慧晶片演練)'}).execute()
id2 = doc2.get('documentId')
docs_service.documents().batchUpdate(documentId=id2, body={'requests': [{'insertText': {'location': {'index': 1}, 'text': "運動會籌備會議紀錄\n\n【硬體租借區段】\n1. 音響與舞台設備租借 - 負責人：[請在此處輸入 @People 指派成員]，完成期限：[請在此處輸入 @Date 設定日期]\n2. 遮陽帳棚 10 頂 - 負責人：[請在此處輸入 @People 指派成員]，完成期限：[請在此處輸入 @Date 設定日期]\n\n【宣傳與競賽區段】\n1. 秩序冊印製 - 負責人：[請在此處輸入 @People 指派成員]，完成期限：[請在此處輸入 @Date 設定日期]\n"}}]}).execute()
make_public(id2)
real_links["Task 02"] = {"title": "運動會籌備會議紀錄 (智慧晶片演練)", "type": "Docs", "url": f"https://docs.google.com/document/d/{id2}/edit?usp=sharing"}

# Task 03
doc3 = docs_service.documents().create(body={'title': '校本課程實施計畫手冊 (段落樣式與目錄演練)'}).execute()
id3 = doc3.get('documentId')
docs_service.documents().batchUpdate(documentId=id3, body={'requests': [{'insertText': {'location': {'index': 1}, 'text': "校本課程實施計畫手冊\n\n[請在此處選取下方的章節名稱，套用段落樣式「標題 1」，並在頂部插入「目錄」]\n\n第一章：課程發展願景與核心素養\n本校課程以自主學習與國際視野為核心...\n\n第二章：全學期課程主題與領域配課\n涵蓋國文、英語、數理與跨領域實作專題...\n\n第三章：多元評量與學習歷程檔案規範\n強調形成性評量與學生自主學習記錄...\n"}}]}).execute()
make_public(id3)
real_links["Task 03"] = {"title": "校本課程實施計畫手冊 (段落樣式與目錄演練)", "type": "Docs", "url": f"https://docs.google.com/document/d/{id3}/edit?usp=sharing"}

# Task 04
doc4 = docs_service.documents().create(body={'title': '國文作文範本 (語音回饋外掛演練)'}).execute()
id4 = doc4.get('documentId')
docs_service.documents().batchUpdate(documentId=id4, body={'requests': [{'insertText': {'location': {'index': 1}, 'text': "學生期末作文：〈那一刻，我長大了〉\n\n那是一個雨天，我在公車站牌看見一位迷路的小孩...\n這是我第一次體會到幫助別人的快樂。那一次經驗讓我知道，成長不只是年齡的增長，更是內心責任感與同理心的展現。\n\n[研習任務：請透過「擴充功能」安裝 Mote 外掛，並在本段落新增註解錄製語音回饋！]\n"}}]}).execute()
make_public(id4)
real_links["Task 04"] = {"title": "國文作文範本 (語音回饋外掛演練)", "type": "Docs", "url": f"https://docs.google.com/document/d/{id4}/edit?usp=sharing"}

# Task 05
doc5 = docs_service.documents().create(body={'title': '班級每週學習通訊 (多語言翻譯演練)'}).execute()
id5 = doc5.get('documentId')
docs_service.documents().batchUpdate(documentId=id5, body={'requests': [{'insertText': {'location': {'index': 1}, 'text': "班級每週學習通訊 (第 8 週)\n\n親愛的家長您好：\n本週班上進行了自然科學戶外觀察，學生表現相當優異。\n提醒您：下週三將舉行期中親師座談會，誠摯邀請您蒞臨參加！\n\n[研習任務：請點選選單「工具 -> 翻譯文件」，選擇目標語言（如越南語或印尼語），自動生成翻譯副本！]\n"}}]}).execute()
make_public(id5)
real_links["Task 05"] = {"title": "班級每週學習通訊 (多語言翻譯演練)", "type": "Docs", "url": f"https://docs.google.com/document/d/{id5}/edit?usp=sharing"}

# Task 13 (Slides)
slide13 = slides_service.presentations().create(body={'title': '英檢單字互動記憶卡 (超連結演練)'}).execute()
id13 = slide13.get('presentationId')
make_public(id13)
real_links["Task 13"] = {"title": "英檢單字互動記憶卡 (超連結演練)", "type": "Slides", "url": f"https://docs.google.com/presentation/d/{id13}/edit?usp=sharing"}

# Task 14 (Slides)
slide14 = slides_service.presentations().create(body={'title': '學校簡報標準母版 (主題建構工具演練)'}).execute()
id14 = slide14.get('presentationId')
make_public(id14)
real_links["Task 14"] = {"title": "學校簡報標準母版 (主題建構工具演練)", "type": "Slides", "url": f"https://docs.google.com/presentation/d/{id14}/edit?usp=sharing"}

# Task 15 (Slides)
slide15 = slides_service.presentations().create(body={'title': '校園植物導覽簡報 (影片內嵌與指派演練)'}).execute()
id15 = slide15.get('presentationId')
make_public(id15)
real_links["Task 15"] = {"title": "校園植物導覽簡報 (影片內嵌與指派演練)", "type": "Slides", "url": f"https://docs.google.com/presentation/d/{id15}/edit?usp=sharing"}

# Task 18 (Sheets)
sheet18 = sheets_service.spreadsheets().create(body={'properties': {'title': '期中測驗成績單 (條件式格式演練)'}}).execute()
id18 = sheet18.get('spreadsheetId')
values18 = [
    ["學生姓名", "數學成績", "英文成績", "自然成績"],
    ["張小明", 85, 92, 78],
    ["李美麗", 55, 68, 48],
    ["王大同", 95, 88, 92],
    ["陳志強", 42, 59, 65],
    ["林雅婷", 78, 85, 52]
]
sheets_service.spreadsheets().values().update(spreadsheetId=id18, range="A1", valueInputOption="USER_ENTERED", body={'values': values18}).execute()
make_public(id18)
real_links["Task 18"] = {"title": "期中測驗成績單 (條件式格式演練)", "type": "Sheets", "url": f"https://docs.google.com/spreadsheet/d/{id18}/edit?usp=sharing"}

# Task 19 (Sheets)
sheet19 = sheets_service.spreadsheets().create(body={'properties': {'title': '運動會進場服裝投票紀錄 (直行統計與樞紐演練)'}}).execute()
id19 = sheet19.get('spreadsheetId')
values19 = [
    ["學生Email", "選擇的服裝顏色", "尺寸"],
    ["student01@school.edu", "亮紅色", "M"],
    ["student02@school.edu", "寶藍色", "L"],
    ["student03@school.edu", "亮紅色", "S"],
    ["student04@school.edu", "亮黃色", "M"],
    ["student05@school.edu", "寶藍色", "M"],
    ["student06@school.edu", "亮紅色", "L"],
    ["student07@school.edu", "寶藍色", "XL"],
    ["student08@school.edu", "亮紅色", "M"]
]
sheets_service.spreadsheets().values().update(spreadsheetId=id19, range="A1", valueInputOption="USER_ENTERED", body={'values': values19}).execute()
make_public(id19)
real_links["Task 19"] = {"title": "運動會進場服裝投票紀錄 (直行統計與樞紐演練)", "type": "Sheets", "url": f"https://docs.google.com/spreadsheet/d/{id19}/edit?usp=sharing"}

# Create docs for Task 06-12, 16-17, 20-25
task_titles = {
    6: "教師自主學習諮詢預約系統 (預約時間表演練)",
    7: "跨校線上講座 (Meet直播演練)",
    8: "社區公聽會邀請函 (權限演練)",
    9: "教研會會議紀錄 (日曆連動演練)",
    10: "雙語協同教學課程指引 (協同教師演練)",
    11: "單元線上形成性評量表單 (成績匯入演練)",
    12: "社會科小論文範例 (原創性比對演練)",
    16: "自然科學小組專題展示網站 (子頁面演練)",
    17: "高中生學習歷程檔案 (發布權限演練)",
    20: "山區戶外觀察即時語音會議 (電話撥號演練)",
    21: "理化自主複習題組 (練習組提示演練)",
    22: "同科備課共享題組 (題組共用演練)",
    23: "翻轉課堂先備知識檢測表單 (區段跳轉演練)",
    24: "科室公用信箱代理授權指引 (帳戶代理演練)",
    25: "文件內即時視訊邊看邊修範本 (檔案內Meet演練)"
}

for idx, title in task_titles.items():
    key = f"Task {idx:02d}"
    doc = docs_service.documents().create(body={'title': f"{title}"}).execute()
    t_id = doc.get('documentId')
    docs_service.documents().batchUpdate(documentId=t_id, body={'requests': [{'insertText': {'location': {'index': 1}, 'text': f"{title}\n\n請根據研習講義步驟，在此真實 Google Workspace 檔案中進行功能實操演練！\n"}}]}).execute()
    make_public(t_id)
    real_links[key] = {"title": title, "type": "Docs", "url": f"https://docs.google.com/document/d/{t_id}/edit?usp=sharing"}

out_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\all_25_real_workspace_links.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(real_links, f, ensure_ascii=False, indent=2)

print("Saved all 25 links!")
