import shutil, os

src_header = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787115463627.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_header = os.path.join(dest_dir, 'gmail_delegated_sent_email_header.png')
shutil.copy2(src_header, dst_header)
print("Copied Gmail delegated sent email header image!")

sent_header_html = '''
          <!-- 7. 最終震撼效果：收件者看到的寄件者標記 -->
          <div style="background:#e8f0fe; border:1.5px solid #1a73e8; border-radius:10px; padding:16px; margin-top:16px;">
            <p style="font-weight:700; font-size:0.92rem; color:#1557b0; margin-bottom:8px;">
              📷 7. 最終收件者視覺效果：清楚顯示【代表主管】與【實際代理人】！
            </p>
            <div style="background:white; border:1px solid #c2e7ff; border-radius:8px; padding:12px; text-align:center; margin-bottom:10px;">
              <img src="images/gmail_delegated_sent_email_header.png" alt="Gmail 代理人代發信寄件者顯示效果" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.9rem; color:#202124; line-height:1.7;">
              🎯 <strong>標題解析</strong>：<code>kuo jung wu &lt;wukolo1206@gmail.com&gt; (寄件者 wukuojung1206@gmail.com)</code>
              <ul style="padding-left:20px; color:#3c4043; margin-top:4px;">
                <li><strong>前半段</strong>：代表的主管/公用帳號（收件者知道這是教務處或組長的正式信函）。</li>
                <li><strong>後半段 <code>(寄件者...)</code></strong>：由系統自動標記真實經手代發的助理帳號，<strong>責任歸屬 100% 清楚無可造假</strong>！</li>
              </ul>
            </div>
          </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_outcome = '<li><strong>最高資安防護</strong>：代理人<strong>無法</strong>修改主管密碼、無法進入主管的私密雲端硬碟，主管可隨時一秒撤銷授權！</li>\n                </ul>\n              </div>\n            </div>\n          </div>'
if 'gmail_delegated_sent_email_header.png' not in h_gmail and target_outcome in h_gmail:
    h_gmail = h_gmail.replace(target_outcome, target_outcome + '\n' + sent_header_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded sent header in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'gmail_delegated_sent_email_header.png' not in h_tasks and target_outcome in h_tasks:
    h_tasks = h_tasks.replace(target_outcome, target_outcome + '\n' + sent_header_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded sent header in hands_on_tasks_app.html!")

# 3. Update Markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_img_add4 = '''
![Gmail 代理人代發信寄件者顯示效果](../images/gmail_delegated_sent_email_header.png)
*圖 7：最終成果——收件者端清楚顯示「主管帳號 (寄件者 代理人帳號)」，責任歸屬一目了然！*
'''

if 'gmail_delegated_sent_email_header.png' not in h_md:
    h_md = h_md.replace('*圖 6：代理人點擊右上角個人頭像，選擇「已委派 (Delegated)」帳戶即可免密碼切換進入！*', '*圖 6：代理人點擊右上角個人頭像，選擇「已委派 (Delegated)」帳戶即可免密碼切換進入！*\n' + md_img_add4)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded sent header in markdown manual!")

print("All files updated with sent header screenshot!")
