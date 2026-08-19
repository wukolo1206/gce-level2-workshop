import shutil, os

src_email = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787115103182.png'
src_accept = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787115118734.png'

dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_email = os.path.join(dest_dir, 'gmail_delegate_invitation_email.png')
dst_accept = os.path.join(dest_dir, 'gmail_delegate_accept_confirmation.png')

shutil.copy2(src_email, dst_email)
shutil.copy2(src_accept, dst_accept)
print("Copied receiver flow images!")

receiver_flow_html = '''
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#137333; margin-bottom:8px;">📷 4. 代理人收到授權確認信：</p>
              <img src="images/gmail_delegate_invitation_email.png" alt="Gmail 代理人收到授權確認信" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">信件主旨：<code>已授予您 Gmail 帳戶的存取權，接受或拒絕？</code></p>
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#137333; margin-bottom:8px;">📷 5. 點擊連結確認完成接受：</p>
              <img src="images/gmail_delegate_accept_confirmation.png" alt="Gmail 點擊連結確認接受代理" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">點選「確認」後，即完成所有代理授權綁定手續！</p>
            </div>
          </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_dialog = '<p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">發送後，對方信箱會收到一封確認信，點擊「接受」後即完成代理人授權！</p>\n          </div>'
if 'gmail_delegate_invitation_email.png' not in h_gmail and target_dialog in h_gmail:
    h_gmail = h_gmail.replace(target_dialog, target_dialog + '\n' + receiver_flow_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded receiver flow in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'gmail_delegate_invitation_email.png' not in h_tasks and target_dialog in h_tasks:
    h_tasks = h_tasks.replace(target_dialog, target_dialog + '\n' + receiver_flow_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded receiver flow in hands_on_tasks_app.html!")

# 3. Update Markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_img_add2 = '''
![Gmail 代理人收到授權確認信](../images/gmail_delegate_invitation_email.png)
*圖 4：代理人信箱收到之授權確認信（點擊接受存取要求連結）*

![Gmail 點擊連結確認接受代理](../images/gmail_delegate_accept_confirmation.png)
*圖 5：點選「確認」完成接受代理人授權*
'''

if 'gmail_delegate_invitation_email.png' not in h_md:
    h_md = h_md.replace('*圖 3：授予存取權確認對話框（點擊「傳送電子郵件以授予存取權」）*', '*圖 3：授予存取權確認對話框（點擊「傳送電子郵件以授予存取權」）*\n' + md_img_add2)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded receiver flow in markdown manual!")

print("All files updated with full delegation lifecycle!")
