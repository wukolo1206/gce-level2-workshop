import os
import re

root = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

# 1. Update lab_exercises_app.html
lab_app_path = os.path.join(root, 'lab_exercises_app.html')
with open(lab_app_path, 'r', encoding='utf-8') as f:
    lab_app_html = f.read()

# Insert image cards into Lab 1, Lab 2, Lab 3 sections in lab_exercises_app.html
lab1_img_card = '''
    <div style="margin-bottom:24px; text-align:center; background:#f8f9fa; padding:16px; border-radius:12px; border:1px solid #dadce0;">
      <img src="images/lab1_classroom_tasks.jpg" style="max-width:100%; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.1);" alt="Lab 1 Google Classroom 實作介面實景圖">
      <div style="font-size:0.88rem; color:#5f6368; margin-top:8px; font-style:italic;">▲ 圖 L-1：Google Classroom Lab 1 實作設定完成介面對照（含 Flipped Class、Term 1/2 主題、Unit 1 作業與 Meet 公告）</div>
    </div>
'''

lab2_img_card = '''
    <div style="margin-bottom:24px; text-align:center; background:#f8f9fa; padding:16px; border-radius:12px; border:1px solid #dadce0;">
      <img src="images/lab2_calendar_livestream.jpg" style="max-width:100%; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.1);" alt="Lab 2 Google Calendar 實作介面實景圖">
      <div style="font-size:0.88rem; color:#5f6368; margin-top:8px; font-style:italic;">▲ 圖 L-2：Google Calendar Lab 2 實作設定完成介面對照（含 Community Fair、Meet 串流直播 Live stream、123 Main Street 與 Email 提醒）</div>
    </div>
'''

lab3_img_card = '''
    <div style="margin-bottom:24px; text-align:center; background:#f8f9fa; padding:16px; border-radius:12px; border:1px solid #dadce0;">
      <img src="images/lab3_slides_comment_assign.jpg" style="max-width:100%; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.1);" alt="Lab 3 Google Slides 實作介面實景圖">
      <div style="font-size:0.88rem; color:#5f6368; margin-top:8px; font-style:italic;">▲ 圖 L-3：Google Slides Lab 3 實作設定完成介面對照（含 Welcome to Our Team、圖片預留位置、內嵌影片與 +Email 批註指派）</div>
    </div>
'''

if 'lab1_classroom_tasks.jpg' not in lab_app_html:
    lab_app_html = lab_app_html.replace('<div id="view-lab1">', '<div id="view-lab1">\n' + lab1_img_card)
    lab_app_html = lab_app_html.replace('<div id="view-lab2" style="display:none;">', '<div id="view-lab2" style="display:none;">\n' + lab2_img_card)
    lab_app_html = lab_app_html.replace('<div id="view-lab3" style="display:none;">', '<div id="view-lab3" style="display:none;">\n' + lab3_img_card)

with open(lab_app_path, 'w', encoding='utf-8') as f:
    f.write(lab_app_html)

print("Successfully updated lab_exercises_app.html with UI screenshots!")

# 2. Update markdown files in docs/
docs_mapping = {
    'GCE_Level_2_Lab_1_Classroom_實作題完整指南.md': ('lab1_classroom_tasks.jpg', 'Google Classroom Lab 1 實作設定完成介面示意圖'),
    'GCE_Level_2_Lab_2_Calendar_實作題完整指南.md': ('lab2_calendar_livestream.jpg', 'Google Calendar Lab 2 實作設定完成介面示意圖'),
    'GCE_Level_2_Lab_3_Slides_實作題完整指南.md': ('lab3_slides_comment_assign.jpg', 'Google Slides Lab 3 實作設定完成介面示意圖')
}

for fname, (img_name, caption) in docs_mapping.items():
    fpath = os.path.join(root, 'docs', fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if img_name not in content:
            img_md = f"\n\n![{caption}](../images/{img_name})\n*▲ 圖：{caption}*\n\n"
            content = content.replace('---', '---' + img_md, 1)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully embedded screenshot into docs/{fname}")

print("\nScreenshot embedding completed!")
