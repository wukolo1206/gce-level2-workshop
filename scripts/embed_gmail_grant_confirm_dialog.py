import shutil, os, subprocess

src_confirm = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787115035085.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_confirm = os.path.join(dest_dir, 'gmail_grant_access_confirm_dialog.png')
shutil.copy2(src_confirm, dst_confirm)
print("Copied Gmail grant access confirmation dialog image!")

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

confirm_card_html = '''
          <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:14px; margin-top:14px; text-align:center;">
            <p style="font-weight:700; font-size:0.85rem; color:#7627bb; margin-bottom:8px;">📷 3. 授予存取權確認對話框（點擊「傳送電子郵件以授予存取權」發出邀請）：</p>
            <img src="images/gmail_grant_access_confirm_dialog.png" alt="Gmail 授予存取權確認對話框" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">發送後，對方信箱會收到一封確認信，點擊「接受」後即完成代理人授權！</p>
          </div>
'''

if 'gmail_grant_access_confirm_dialog.png' not in h_gmail:
    h_gmail = h_gmail.replace('<!-- 個人版 vs 教育版 Gmail 介面差異對照卡片 -->', '<!-- 個人版 vs 教育版 Gmail 介面差異對照卡片 -->')
    # Insert right inside the comparison card before </div>
    target_pos = '<!-- 個人版 vs 教育版 Gmail 介面差異對照卡片 -->'
    # Find the end of comparison card
    h_gmail = h_gmail.replace('<li><strong>注意防呆</strong>：請勿點選「選擇寄件地址」中的「新增另一個電子郵件地址」（那是別名寄件，非帳戶代理）。</li>\n            </ul>\n          </div>\n        </div>', '<li><strong>注意防呆</strong>：請勿點選「選擇寄件地址」中的「新增另一個電子郵件地址」（那是別名寄件，非帳戶代理）。</li>\n            </ul>\n          </div>\n' + confirm_card_html + '\n        </div>')
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded confirm dialog in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html Task 24
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'gmail_grant_access_confirm_dialog.png' not in h_tasks:
    h_tasks = h_tasks.replace('<li><strong>注意防呆</strong>：請勿點選「選擇寄件地址」中的「新增另一個電子郵件地址」（那是別名寄件，非帳戶代理）。</li>\n            </ul>\n          </div>\n        </div>', '<li><strong>注意防呆</strong>：請勿點選「選擇寄件地址」中的「新增另一個電子郵件地址」（那是別名寄件，非帳戶代理）。</li>\n            </ul>\n          </div>\n' + confirm_card_html + '\n        </div>')
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded confirm dialog in hands_on_tasks_app.html!")

# 3. Update markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_img_add = '''
![Gmail 授予存取權確認對話框](../images/gmail_grant_access_confirm_dialog.png)
*圖 3：授予存取權確認對話框（點擊「傳送電子郵件以授予存取權」）*
'''

if 'gmail_grant_access_confirm_dialog.png' not in h_md:
    h_md = h_md.replace('*圖 2：學校教育版帳號（分頁為「帳戶」，若教育局管理後台關閉委派，此功能會被系統隱藏）*', '*圖 2：學校教育版帳號（分頁為「帳戶」，若教育局管理後台關閉委派，此功能會被系統隱藏）*\n' + md_img_add)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded confirm dialog in markdown manual!")

print("Files updated! Now running deploy_to_github_pages.py...")
