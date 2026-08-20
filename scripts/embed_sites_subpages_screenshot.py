import shutil, os

# 1. Save user's screenshot showing the successful subpages dropdown
src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787205208401.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'sites_subpages_dropdown_menu.png')
shutil.copy2(src_img, dst_img)
print("Copied Sites subpages dropdown screenshot!")

# 2. HTML Card for sites_workshop_app.html Module 1
subpages_card_html = '''
        <!-- 🗂️ 子頁面階層結構與頂部下拉選單成果圖解卡片 -->
        <div style="background:#ffffff; border:2px solid #00897b; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(0,137,123,0.1);">
          <h3 style="color:#00695c; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            🗂️ 實務介面圖解：【子頁面縮排階層】與【頂部導覽列下拉選單】
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            在 Google 協作平台中，只要將小組頁面<strong>拖曳收納至母頁面底下（形成子頁面）</strong>，頂部導覽列就會自動生成整齊的下拉式選單：
          </p>

          <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#00695c; margin-bottom:8px;">📷 成果展示：右側子頁面縮排 ➔ 頂部「首頁 ▾」下拉選單：</p>
              <img src="images/sites_subpages_dropdown_menu.png" alt="Google Sites 子頁面與頂部下拉選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#00695c; font-size:0.95rem;">⚡ 兩大建立子頁面的關鍵技巧：</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>極速拖曳法</strong>：直接在右側「頁面」清單中，按住「第一組」拖曳到「首頁」上方放開，瞬間變成子頁面！</li>
                <li><strong>三點選單法</strong>：滑鼠移到母頁面右側 <code>三點圖示 ➔ 新增子頁面 (Add subpage)</code>。</li>
                <li><strong>自動生成導覽</strong>：不用手動寫程式或設定連結，系統會自動在頂端產生 <code>首頁 ▾</code> 下拉選單！</li>
              </ul>
            </div>
          </div>
        </div>
'''

p_sites = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'sites_workshop_app.html')
with open(p_sites, 'r', encoding='utf-8') as f:
    h_sites = f.read()

target_m1_sites = '<h2>建立網站並為各小組新增專屬子頁面 (Subpages)</h2>'
if target_m1_sites in h_sites and 'sites_subpages_dropdown_menu.png' not in h_sites:
    h_sites = h_sites.replace(target_m1_sites, target_m1_sites + '\n' + subpages_card_html)
    with open(p_sites, 'w', encoding='utf-8') as f:
        f.write(h_sites)
    print("Embedded subpages screenshot in sites_workshop_app.html!")

# 3. Update hands_on_tasks_app.html Task 16
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'sites_subpages_dropdown_menu.png' not in h_tasks and '為各小組新增專屬子頁面' in h_tasks:
    h_tasks = h_tasks.replace('<h2>建立網站並為各小組新增專屬子頁面', subpages_card_html + '\n<h2>建立網站並為各小組新增專屬子頁面')
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded subpages screenshot in hands_on_tasks_app.html!")

# 4. Update Markdown manual Task 16
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_sites_guide = '''
##### 🗂️ Sites 實務介面圖解：子頁面階層與頂部導覽列下拉選單
![Google Sites 子頁面與頂部下拉選單](../images/sites_subpages_dropdown_menu.png)
*圖 15：右側「頁面」面板將小組縮排為子頁面，頂部導覽列自動形成「首頁 ▾」下拉式選單*

> 💡 **核心操作技巧**：
> 1. **拖曳法**：在右側面板按住子頁面，拖曳丟到母頁面上放開即可建立階層。
> 2. **三點圖示**：母頁面旁點擊 `三點 ➔ 新增子頁面 (Add subpage)`。
> 3. **效果驗證**：頂部導覽列自動收合為下拉選單，避免頁面過多造成版面擁擠！
'''

if 'sites_subpages_dropdown_menu.png' not in h_md and '#### 演練 16' in h_md:
    h_md = h_md.replace('#### 演練 16', '#### 演練 16\n' + md_sites_guide)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded subpages guide in markdown manual!")

print("All Sites documentation updated! Ready to deploy.")
