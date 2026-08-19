import shutil, os

src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787116318463.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'gmail_save_and_insert_template_menu.png')
shutil.copy2(src_img, dst_img)
print("Copied Gmail save and insert template menu image!")

template_menu_html = '''
          <!-- 8. 實務操作：在信件中儲存與插入範本 -->
          <div style="background:#f8f9fa; border:1.5px solid #1a73e8; border-radius:10px; padding:16px; margin-top:16px;">
            <p style="font-weight:700; font-size:0.92rem; color:#1557b0; margin-bottom:8px;">
              📷 8. 實務操作：撰寫信件時，由右下角【三點選單 ➔ 範本】儲存或套用：
            </p>
            <div style="background:white; border:1px solid #c2e7ff; border-radius:8px; padding:12px; text-align:center; margin-bottom:10px;">
              <img src="images/gmail_save_and_insert_template_menu.png" alt="Gmail 撰寫信件儲存與套用範本選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.9rem; color:#202124; line-height:1.7;">
              🎯 <strong>標準兩步驟</strong>：
              <ul style="padding-left:20px; color:#3c4043; margin-top:4px;">
                <li><strong>儲存為新範本</strong>：草稿打好後 ➔ 點右下角 <code>三點 ➔ 範本 ➔ 將草稿儲存為範本 ➔ 另存為新範本</code>。</li>
                <li><strong>未來一鍵插入</strong>：開新信時 ➔ 點右下角 <code>三點 ➔ 範本 ➔ 點選「校外教學通知」</code> 即可瞬間填滿！</li>
              </ul>
            </div>
          </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_end = '💡 <strong>操作提示</strong>：複製上方整段文章，在 Gmail 點「撰寫」貼上主旨與內文，再點右下角 <code>三點 ➔ 範本 ➔ 將草稿儲存為範本 ➔ 另存為新範本</code> 即可！\n            </p>\n          </div>\n        </div>'
if 'gmail_save_and_insert_template_menu.png' not in h_gmail and target_end in h_gmail:
    h_gmail = h_gmail.replace(target_end, target_end + '\n' + template_menu_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded template menu image in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'gmail_save_and_insert_template_menu.png' not in h_tasks and target_end in h_tasks:
    h_tasks = h_tasks.replace(target_end, target_end + '\n' + template_menu_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded template menu image in hands_on_tasks_app.html!")

# 3. Update Markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_img_add6 = '''
![Gmail 撰寫信件儲存與套用範本選單](../images/gmail_save_and_insert_template_menu.png)
*圖 8：撰寫郵件時，由右下角「三點 ➔ 範本 ➔ 將草稿儲存為範本」儲存或一鍵套用範本！*
'''

if 'gmail_save_and_insert_template_menu.png' not in h_md:
    target_md = '導師 敬上\n\'\'\''
    if target_md in h_md:
        h_md = h_md.replace(target_md, target_md + '\n' + md_img_add6)
    else:
        h_md = h_md.replace('導師 敬上', '導師 敬上\n' + md_img_add6)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded template menu image in markdown manual!")

print("All files updated with save template menu!")
