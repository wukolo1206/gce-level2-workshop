import shutil, os, subprocess

src_personal = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787114761670.png'
src_edu = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787114770940.png'

dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_personal = os.path.join(dest_dir, 'gmail_settings_personal_account.png')
dst_edu = os.path.join(dest_dir, 'gmail_settings_education_workspace.png')

shutil.copy2(src_personal, dst_personal)
shutil.copy2(src_edu, dst_edu)
print("Copied Gmail account comparison images!")

comparison_html = '''
        <!-- 個人版 vs 教育版 Gmail 介面差異對照卡片 -->
        <div style="background:#ffffff; border:1.5px solid #9334e6; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 3px 12px rgba(147,52,230,0.08);">
          <h3 style="color:#7627bb; margin-top:0; font-size:1.15rem; display:flex; align-items:center; gap:8px;">
            🔍 實務介面對照：個人版 (@gmail.com) vs 學校教育版 (@apps.ntpc.edu.tw)
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; margin-bottom:14px;">
            在研習上機時，許多老師會發現自己的 Gmail 設定畫面長得不一樣，這是因為<strong>個人帳號與教育局/學校 Workspace 網域權限不同</strong>：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 1. 個人 Gmail 帳號（@gmail.com）：</p>
              <img src="images/gmail_settings_personal_account.png" alt="個人版 Gmail 帳戶和匯入設定" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">分頁名稱為<strong>「帳戶和匯入」</strong>，預設完整開放「授予您帳戶的存取權」</p>
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#c5221f; margin-bottom:8px;">📷 2. 學校教育版帳號（@apps.ntpc.edu.tw）：</p>
              <img src="images/gmail_settings_education_workspace.png" alt="教育版 Gmail 帳戶設定" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">分頁名稱為<strong>「帳戶」</strong>，若教育局管理後台關閉委派，此功能會被系統隱藏</p>
            </div>
          </div>

          <div style="background:#fef7e0; border-left:4px solid #f9ab00; border-radius:0 8px 8px 0; padding:14px; font-size:0.9rem; line-height:1.7;">
            <div style="font-weight:700; color:#b06000; margin-bottom:6px;">💡 研習實作與備考指南：</div>
            <ul style="padding-left:20px; color:#3c4043;">
              <li><strong>現場上機演練</strong>：請老師們使用<strong>個人 @gmail.com 帳號</strong>兩人一組互相新增代理人，可 100% 順暢演練「邀請與接受」流程。</li>
              <li><strong>認證考試標準路徑</strong>：在 Level 2 考試中，標準解題路徑為：<code>設定 (右上齒輪) ➔ 查看所有設定 ➔ 帳戶與匯入 ➔ 授予您帳戶的存取權 ➔ 新增其他帳戶</code>！</li>
              <li><strong>注意防呆</strong>：請勿點選「選擇寄件地址」中的「新增另一個電子郵件地址」（那是別名寄件，非帳戶代理）。</li>
            </ul>
          </div>
        </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_gmail = '<h2>授予您帳戶的存取權 (Grant access to your account) 代收代發</h2>'
if target_gmail in h_gmail and 'gmail_settings_personal_account.png' not in h_gmail:
    h_gmail = h_gmail.replace(target_gmail, target_gmail + '\n' + comparison_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded comparison card in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

target_task24 = '<h2 class="task-title">教務處公用信箱代理人授權與交接</h2>'
if target_task24 in h_tasks and 'gmail_settings_personal_account.png' not in h_tasks:
    h_tasks = h_tasks.replace(target_task24, target_task24 + '\n' + comparison_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded comparison card in hands_on_tasks_app.html!")

print("All HTML files updated with Gmail account comparison!")
