import shutil, os

src1 = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787113837447.png'
src2 = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787114033448.png'

dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dest1 = os.path.join(dest_dir, 'theme_builder_master_structure.png')
dest2 = os.path.join(dest_dir, 'apply_layout_templates_menu.png')

shutil.copy2(src1, dest1)
shutil.copy2(src2, dest2)
print("Copied images to project directory!")

# Explanation card HTML to embed in slides_workshop_app.html
explanation_html = '''
        <!-- 母片結構與版面配置邏輯深入解析卡片 -->
        <div style="background:#ffffff; border:1.5px solid #4285f4; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 3px 12px rgba(66,133,244,0.08);">
          <h3 style="color:#1a73e8; margin-top:0; font-size:1.15rem; display:flex; align-items:center; gap:8px;">
            🧩 觀念釐清：母片階層邏輯與「套用版面配置」的對應關係
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; margin-bottom:14px;">
            在進入實作前，先理解 Google Slides 的<strong>「三層繼承架構」</strong>，這能讓您在製作全校公用模板時完全不踩雷：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 1. 主題製作工具（後台模具工廠）：</p>
              <img src="images/theme_builder_master_structure.png" alt="主題製作工具母片結構" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">頂部是全域「主題母片」，下方縮排是一張張「版面配置 (Layouts)」</p>
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#137333; margin-bottom:8px;">📷 2. 套用版面配置（前台套用模板）：</p>
              <img src="images/apply_layout_templates_menu.png" alt="套用版面配置選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">一般畫面中挑選的「模板選單」，與左側模具工廠<strong>一對一完全對應</strong>！</p>
            </div>
          </div>

          <div style="background:#f8f9fa; border-radius:8px; padding:14px; font-size:0.9rem; line-height:1.7;">
            <div style="margin-bottom:8px;">
              <strong style="color:#1a73e8;">👑 1. 最頂端大張【主題母片】（總指揮官）</strong>：<br>
              負責定義全校統一字型、背景色、角落校徽 Logo、頁碼。<strong>只要動這 1 張，整份簡報所有頁面自動全部套用</strong>！
            </div>
            <div style="margin-bottom:8px;">
              <strong style="color:#137333;">📑 2. 底下縮排的十幾張【版面配置 (Layouts)】（各場景模具）</strong>：<br>
              針對不同教學場景（封面、內文、雙欄、照片展示）設計專用模具。您在此新增的「圖片預留位置」，會直接呈現在前台的「套用版面配置」選單中供教師一鍵套用！
            </div>
            <div>
              <strong style="color:#b06000;">🛡️ 3. 防呆保護機制</strong>：<br>
              畫在母片／版面配置中的物件，回到一般編輯模式下<strong>點不到、刪不掉</strong>，能確保全校同仁製作簡報時不會不小心改壞格式與校徽！
            </div>
          </div>
        </div>
'''

# Update slides_workshop_app.html
path_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\slides_workshop_app.html'
with open(path_app, 'r', encoding='utf-8') as f:
    html = f.read()

target = '<h2>使用主題製作工具 (Theme builder) 插入圖片預留位置 (Placeholder)</h2>'
if target in html and 'theme_builder_master_structure.png' not in html:
    html = html.replace(target, target + '\n' + explanation_html)
    with open(path_app, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Embedded master structure explanation and images in slides_workshop_app.html!")

# Update hands_on_tasks_app.html Task 14
path_tasks = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_tasks, 'r', encoding='utf-8') as f:
    t_html = f.read()

task14_target = '<h2 class="task-title">學校簡報標準母版與主題建構</h2>'
if task14_target in t_html and 'theme_builder_master_structure.png' not in t_html:
    t_html = t_html.replace(task14_target, task14_target + '\n' + explanation_html)
    with open(path_tasks, 'w', encoding='utf-8') as f:
        f.write(t_html)
    print("Embedded master structure explanation in hands_on_tasks_app.html!")

print("All embeddings complete!")
