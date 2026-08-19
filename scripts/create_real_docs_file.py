import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = r'd:\備課ai\google workspace\token.json'
creds = Credentials.from_authorized_user_file(token_path)

drive_service = build('drive', 'v3', credentials=creds)
docs_service = build('docs', 'v1', credentials=creds)

# 1. Create a new Google Docs document
doc_title = "全校週報範例 (研習實作檔 - 尋找與取代演練)"
doc = docs_service.documents().create(body={'title': doc_title}).execute()
doc_id = doc.get('documentId')
print(f"Created Document ID: {doc_id}")

# 2. Insert sample text with misspelled principal name "陳大文" multiple times
sample_content = """全校週報第 102 期 - 教學與行政重點宣導

【校長的話】
歡迎全體師生來到新學期！陳大文校長在本週晨會中致詞表示，本學年學校將全力推動數位雙語教學與跨領域專案。陳大文校長特別強調，每一位同仁的辛勞都是學校進步的基石。

【行政公告】
1. 本週五下午將召開全校教職員會議，請陳大文校長主持會議，請各處室主任準時出席。
2. 感謝陳大文校長指導教務處完成本學期校本課程計畫書編撰。

【榮譽榜】
狂賀！本校參加全國科展榮獲特優，陳大文校長將於下週頒發獎狀與獎學金表揚獲獎師生。感謝陳大文校長的殷切指導！

【學務處通知】
本週防震演練將由陳大文校長親自指揮，請全校師生依指引進行避難演練。演練結束後陳大文校長將進行全校講評。

【備註】
請學員使用 Google Docs 的快捷鍵 Ctrl + H（尋找與取代功能），將本文件中所有的舊校長姓名「陳大文」，一次性全部取代更正為新校長姓名「張小明」！
"""

docs_service.documents().batchUpdate(documentId=doc_id, body={
    'requests': [
        {
            'insertText': {
                'location': {'index': 1},
                'text': sample_content
            }
        }
    ]
}).execute()

# 3. Set permission to anyone with link can view (or edit)
permission_body = {
    'role': 'writer',  # allow edit or view
    'type': 'anyone'
}
drive_service.permissions().create(fileId=doc_id, body=permission_body).execute()

shareable_link = f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
print(f"Shareable Google Docs Link: {shareable_link}")

# Save the link to a JSON file
result = {
    "doc_id": doc_id,
    "title": doc_title,
    "url": shareable_link
}
with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\real_google_docs_link.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Saved link to real_google_docs_link.json!")
