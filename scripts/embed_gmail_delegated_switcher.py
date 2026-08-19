import shutil, os

src_switcher = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787115285562.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_switcher = os.path.join(dest_dir, 'gmail_delegated_account_switcher.png')
shutil.copy2(src_switcher, dst_switcher)
print("Copied Gmail delegated account switcher image!")

outcome_html = '''
          <!-- 6. 成果驗證：右上角帳戶切換器出現已委派帳號 -->
          <div style="background:#f8f9fa; border:1.5px solid #137333; border-radius:10px; padding:16px; margin-top:16px;">
            <div style="display:flex; flex-wrap:wrap; gap:16px; align-items:center;">
              <div style="flex:1; min-width:280px; text-align:center;">
                <p style="font-weight:700; font-size:0.88rem; color:#137333; margin-bottom:8px;">📷 6. 成果驗證：點右上角頭像切換【已委派】信箱：</p>
                <img src="images/gmail_delegated_account_switcher.png" alt="Gmail 右上角切換已委派帳戶" style="max-width:100%; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.12);">
              </div>
              <div style="flex:1.2; min-width:280px; font-size:0.9rem; line-height:1.7;">
                <strong style="color:#137333; font-size:0.98rem;">✨ 代理授權完成後的強大效果：</strong>
                <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                  <li><strong>免密碼一鍵切換</strong>：點選帶有 <code>🔑 已委派</code> 標籤的帳戶，直接開啟獨立新分頁進入該信箱，免輸密碼！</li>
                  <li><strong>代發信責任歸屬清楚</strong>：寄信時收件者會看到 <code>由「代理人」代表「主管」傳送</code>，清楚記錄經手人。</li>
                  <li><strong>最高資安防護</strong>：代理人<strong>無法</strong>修改主管密碼、無法進入主管的私密雲端硬碟，主管可隨時一秒撤銷授權！</li>
                </ul>
              </div>
            </div>
          </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_step5 = '<p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">點選「確認」後，即完成所有代理授權綁定手續！</p>\n            </div>\n          </div>'
if 'gmail_delegated_account_switcher.png' not in h_gmail and target_step5 in h_gmail:
    h_gmail = h_gmail.replace(target_step5, target_step5 + '\n' + outcome_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded outcome in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'gmail_delegated_account_switcher.png' not in h_tasks and target_step5 in h_tasks:
    h_tasks = h_tasks.replace(target_step5, target_step5 + '\n' + outcome_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded outcome in hands_on_tasks_app.html!")

# 3. Update Markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_img_add3 = '''
![Gmail 右上角切換已委派帳戶](../images/gmail_delegated_account_switcher.png)
*圖 6：代理人點擊右上角個人頭像，選擇「已委派 (Delegated)」帳戶即可免密碼切換進入！*

##### 🛡️ 代理授權 (Grant Access) 核心效果與資安效益：
- **免密碼安全切換**：代理人點選「已委派」帳戶即可開新分頁代收代發，完全不必得知主管密碼。
- **寄件者清楚標記**：信件寄出時收件者會看到 `由「代理人」代表「主管」傳送`，責任歸屬明確。
- **資安完全隔離**：代理人無法變更密碼或查看主管個人雲端硬碟私密檔案，隨時可一鍵撤銷授權。
'''

if 'gmail_delegated_account_switcher.png' not in h_md:
    h_md = h_md.replace('*圖 5：點選「確認」完成接受代理人授權*', '*圖 5：點選「確認」完成接受代理人授權*\n' + md_img_add3)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded outcome in markdown manual!")

print("Files updated with complete delegation lifecycle and outcome!")
