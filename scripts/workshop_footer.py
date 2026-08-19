# -*- coding: utf-8 -*-
"""
全站共用頁尾（單行版）。

法律聲明的完整內容放在 repo 的 LICENSE，頁面上只留一行摘要與連結——
既保有必要聲明（製作者、來源、截圖歸屬、非商業授權），又不佔版面。

由 build_workshop_apps.py／build_course_structure_map.py／
build_exam_registration.py／build_public_index.py 共同引用。

注意：本字串會被插入 f-string 模板，內容中不可出現大括號 { }。
"""

LICENSE_URL = 'https://github.com/wukolo1206/gce-level2-workshop/blob/main/LICENSE'

FOOTER = f'''
  <footer style="max-width:1200px; margin:0 auto; padding:18px 20px 28px; border-top:1px solid #e8eaed;
                 color:#80868b; font-size:.78rem; line-height:1.7; text-align:center;">
    © 2026 碧華國小　吳國榮
    <span style="margin:0 6px; color:#dadce0;">‧</span>參考 Google 官方教材整理改寫，截圖著作權屬 Google LLC
    <span style="margin:0 6px; color:#dadce0;">‧</span>自撰內容採 CC BY-NC-SA 4.0（禁商業使用）
    <span style="margin:0 6px; color:#dadce0;">‧</span><a href="{LICENSE_URL}" target="_blank" rel="noopener"
      style="color:#5f6368;">授權說明與聯絡</a>
  </footer>
'''
