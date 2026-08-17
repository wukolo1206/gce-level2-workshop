# -*- coding: utf-8 -*-
"""
九個工具篇研習 App 的統一產線（取代 build_aligned_tool_apps.py 與
reorder_and_align_scenarios.py）。內容資料放在 workshop_content.py。

核心改良：綠框不再一律掛「一份 Docs」，而是依工具性質給出真正能練的環境——
  copy     檔案型工具 ➔ 網址自動轉 /copy，學員拿到自己的副本
  calendar Calendar   ➔ 產生預填活動網址，直接在學員自己的日曆開草稿
  pair/host/build/demo/license 則說明配對、講師開房、自建與授權限制

用法：python scripts/build_workshop_apps.py
"""
import os
import json
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workshop_content import APPS  # noqa: E402
from workshop_glossary import GLOSSARY  # noqa: E402
from workshop_footer import FOOTER  # noqa: E402

with open(os.path.join(ROOT, 'all_25_real_workspace_links.json'), 'r', encoding='utf-8') as f:
    LINKS = json.load(f)

TYPE_LABEL = {'Docs': 'Google Docs', 'Slides': 'Google 簡報', 'Sheets': 'Google 試算表'}

# 練習型態 ➔ 圖示、標題、配色
STYLE = {
    'copy':     {'icon': '📄', 'label': '複製範本',
                 'head': '本單元練習方式：複製一份範本，改壞了也沒關係',
                 'fg': '#137333', 'bg': '#e6f4ea', 'bd': '#34a853', 'inner': '#a8dab5'},
    'calendar': {'icon': '⚡', 'label': '一鍵建立',
                 'head': '本單元練習方式：一鍵在你自己的日曆建立練習活動',
                 'fg': '#1557b0', 'bg': '#e8f0fe', 'bd': '#1a73e8', 'inner': '#aecbfa'},
    'pair':     {'icon': '👥', 'label': '兩人一組',
                 'head': '本單元練習方式：兩人一組，互相操作才練得到',
                 'fg': '#7627bb', 'bg': '#f3e8fd', 'bd': '#9334e6', 'inner': '#d7aefb'},
    'host':     {'icon': '🎙️', 'label': '講師開房',
                 'head': '本單元練習方式：講師開房間，全體進去實測',
                 'fg': '#b06000', 'bg': '#fef7e0', 'bd': '#f9ab00', 'inner': '#fde293'},
    'build':    {'icon': '🔨', 'label': '自己建一次',
                 'head': '本單元練習方式：從零自己建一次（不需要範本檔）',
                 'fg': '#00695c', 'bg': '#e0f2f1', 'bd': '#00897b', 'inner': '#80cbc4'},
    'demo':     {'icon': '👀', 'label': '觀摩後自建',
                 'head': '本單元練習方式：先看講師示範，再自己建一個',
                 'fg': '#00695c', 'bg': '#e0f2f1', 'bd': '#00897b', 'inner': '#80cbc4'},
    'license':  {'icon': '⚠️', 'label': '需付費授權',
                 'head': '本單元練習方式：需 Education Plus 授權（附一般帳號替代練習）',
                 'fg': '#b3261e', 'bg': '#fce8e6', 'bd': '#d93025', 'inner': '#f6aea9'},
}

LEGEND = [
    ('copy', '點按鈕直接複製一份範本到你的雲端硬碟，隨便改。'),
    ('calendar', '點按鈕在你自己的日曆開一個已填好內容的活動草稿。'),
    ('pair', '需要另一個人才練得到，請和旁邊的夥伴配對。'),
    ('host', '講師會開好會議室或課程，請用現場公布的連結／代碼進入。'),
    ('build', '沒有範本，從空白自己做一次（這類功能自己排過才會懂）。'),
    ('license', '此功能需付費授權，一般帳號請做替代練習。'),
]


def _base(url):
    return url.split('/edit')[0].split('?')[0].rstrip('/')


def copy_url(url):
    """把 /edit?usp=sharing 轉成 /copy，讓學員拿到自己的副本。"""
    return _base(url) + '/copy'


def preview_url(url):
    """純觀摩用連結一律走 /preview 唯讀檢視，避免有人誤改母版。"""
    return _base(url) + '/preview'


def calendar_url(cal):
    """組出 Google Calendar 預填活動網址。"""
    params = {
        'action': 'TEMPLATE',
        'text': cal['text'],
        'dates': cal['dates'],
        'details': cal['details'],
        'location': cal.get('location', ''),
    }
    return 'https://calendar.google.com/calendar/render?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def btn(url, text, color):
    return (f'<a href="{url}" target="_blank" rel="noopener" style="text-decoration:none; background:{color}; color:white; '
            f'padding:10px 22px; border-radius:20px; font-weight:700; font-size:0.92rem; '
            f'box-shadow:0 3px 8px rgba(0,0,0,0.15); white-space:nowrap;">{text}</a>')


def build_practice_box(pr):
    st = STYLE[pr['type']]
    info = LINKS.get(pr.get('task_key', ''), {})
    raw_url = info.get('url', '')
    f_type = info.get('type', 'Docs')

    action = ''       # 右上角按鈕
    body = ''         # 白色內框上半部
    ref = ''          # 底部次要參考連結

    if pr['type'] == 'copy':
        label = TYPE_LABEL.get(f_type, 'Google Docs')
        action = btn(copy_url(raw_url), f'{st["icon"]} 建立我的專屬副本', st['fg'])
        body = (f'<div style="font-size:0.88rem; color:#5f6368; margin-bottom:6px;">'
                f'範本：<strong>{info.get("title", "")}</strong>（{pr.get("task_key", "")} ‧ {label}）</div>'
                f'<div style="font-size:0.86rem; color:#5f6368; margin-bottom:8px;">'
                f'點按鈕後會問你「要建立副本嗎」，按下去就會在<strong>你自己的雲端硬碟</strong>產生一份，'
                f'怎麼改都不會影響別人。</div>')

    elif pr['type'] == 'calendar':
        action = btn(calendar_url(pr['cal']), f'{st["icon"]} 開啟我的練習活動', st['fg'])
        body = (f'<div style="font-size:0.88rem; color:#5f6368; margin-bottom:6px;">'
                f'活動：<strong>{pr["cal"]["text"]}</strong></div>'
                f'<div style="font-size:0.86rem; color:#5f6368; margin-bottom:8px;">'
                f'點按鈕會在<strong>你自己的 Google 日曆</strong>開啟一個已填好標題與說明的新活動草稿'
                f'（尚未儲存，可自行調整時間）。</div>')

    elif pr['type'] == 'pair':
        roles = ''.join(f'<li style="margin-bottom:6px;">{r}</li>' for r in pr.get('roles', []))
        body = (f'<div style="font-size:0.9rem; color:#3c4043; margin-bottom:8px;"><strong>角色分工：</strong>'
                f'<ul style="padding-left:20px; margin-top:6px; line-height:1.7;">{roles}</ul></div>')

    elif pr['type'] == 'host':
        body = (f'<div style="border:1px dashed {st["bd"]}; border-radius:6px; padding:10px 14px; margin-bottom:10px; '
                f'font-size:0.9rem; color:{st["fg"]};">'
                f'🔑 <strong>講師現場公布</strong>：會議連結／課程代碼 ＿＿＿＿＿＿＿＿＿＿</div>')

    elif pr['type'] == 'license':
        body = (f'<div style="font-size:0.9rem; color:{st["fg"]}; font-weight:700; margin-bottom:8px;">'
                f'此功能需 Education Plus 或 Teaching &amp; Learning Upgrade 授權；沒有授權者請直接做下方的替代練習。</div>')

    # 主要任務
    todo = (f'<div style="font-size:0.95rem; color:{st["fg"]}; font-weight:700; line-height:1.6;">'
            f'🎯 你要做的事：<span style="color:#202124; font-weight:500;">{pr["todo"]}</span></div>')

    # 替代練習（license）
    alt = ''
    if pr.get('alt'):
        alt = (f'<div style="background:#fff; border:1px solid #dadce0; border-left:4px solid #1a73e8; border-radius:6px; '
               f'padding:12px 16px; margin-top:10px; font-size:0.92rem; color:#202124; line-height:1.6;">'
               f'🔄 {pr["alt"]}</div>')

    # 補充提醒
    note = ''
    if pr.get('note'):
        note = (f'<div style="font-size:0.88rem; color:#5f6368; margin-top:10px; line-height:1.6; '
                f'border-top:1px dashed {st["inner"]}; padding-top:10px;">💬 {pr["note"]}</div>')

    # 次要參考文件（非 copy 型態時，原本那份說明文件仍保留為選讀；一律唯讀 /preview）
    if pr['type'] not in ('copy',) and raw_url:
        ref = (f'<div style="margin-top:10px; font-size:0.82rem; color:#5f6368;">'
               f'📎 <a href="{preview_url(raw_url)}" target="_blank" rel="noopener" style="color:#5f6368;">'
               f'情境補充說明文件（唯讀，{pr.get("task_key", "")}）</a></div>')

    return f'''
        <div style="background:{st["bg"]}; border:2px solid {st["bd"]}; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:{st["fg"]}; font-size:1.05rem;">{st["icon"]} {st["head"]}</strong>
            {action}
          </div>
          <div style="background:white; border:1px solid {st["inner"]}; border-radius:8px; padding:12px 16px; margin-top:8px;">
            {body}{todo}{alt}{note}
          </div>
          {ref}
        </div>
'''


def build_gate_bar(g):
    """帳號門檻與對應考題提示條。"""
    if not g:
        return ''
    need = (f'<span style="color:#b3261e; font-weight:700;">⚠️ 帳號門檻：</span>'
            f'<span style="color:#3c4043;">{g["need"]}</span>') if g.get('need') else ''
    quiz = (f'<span style="color:#1557b0; font-weight:700;">📝 對應考題：</span>'
            f'<span style="color:#3c4043;">{g["quiz"]}</span>') if g.get('quiz') else ''
    sep = '<span style="color:#dadce0; margin:0 10px;">｜</span>' if need and quiz else ''
    return (f'<div style="background:#fff8e1; border:1px solid #f9ab00; border-radius:8px; '
            f'padding:10px 14px; margin:-4px 0 16px 0; font-size:0.88rem; line-height:1.6;">'
            f'{need}{sep}{quiz}</div>')


def build_module_card(idx, m):
    steps_list = ''
    for s_idx, s in enumerate(m['steps'], 1):
        steps_list += f'''
          <div class="step-item">
            <input type="checkbox" id="m{idx}-s{s_idx}">
            <label for="m{idx}-s{s_idx}">{s}</label>
          </div>'''

    img_html = ''
    if m.get('has_img'):
        img_html = '''
        <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:10px; padding:16px; margin:16px 0; text-align:center;">
          <p style="font-size:0.9rem; font-weight:700; color:#1a73e8; margin-bottom:8px;">📷 Google Docs 插入目錄介面對照圖（選單：插入 ➔ 目錄）：</p>
          <img src="images/docs_insert_toc_menu.png" alt="Google Docs 插入目錄介面截圖" style="max-width:100%; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.12);">
        </div>
'''

    return f'''
      <!-- MODULE {idx} -->
      <div class="module-card" id="module-{idx}" style="display:none;">
        <span class="tag">{m["tag"]}</span>
        <h2>{m["title"]}</h2>
        <p>{m["intro"]}</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          {m["scenario"]}
        </div>

{build_practice_box(m["practice"])}
{img_html}
        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          {steps_list}
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-{idx}')">📋 複製本單元操作步驟</button>
        </div>
      </div>
'''


def build_app(app):
    menu_html = '      <button class="menu-item active" onclick="showModule(0)">🎯 工具篇總覽與研習目標</button>\n'
    for i, m in enumerate(app['modules'], 1):
        menu_html += f'      <button class="menu-item" onclick="showModule({i})">{m["menu"]}</button>\n'

    goals_html = '\n'.join(f'            <li>{g}</li>' for g in app['goals'])

    cards_html = ''.join(build_module_card(i, m) for i, m in enumerate(app['modules'], 1))

    # 本篇實際用到的練習型態，才列進圖例
    used = []
    for m in app['modules']:
        t = m['practice']['type']
        if t not in used:
            used.append(t)
    legend_html = ''
    for t, desc in LEGEND:
        if t in used or (t == 'build' and 'demo' in used):
            st = STYLE[t]
            legend_html += (f'<li style="margin-bottom:6px;"><strong style="color:{st["fg"]};">'
                            f'{st["icon"]} {st["label"]}</strong>　{desc}</li>')

    lic_html = ''
    if app.get('license_warning'):
        lic_html = f'''
        <div style="background:#fce8e6; border:2px solid #d93025; border-radius:12px; padding:16px 20px; margin:20px 0;">
          <strong style="color:#b3261e;">⚠️ 開始前務必確認你的帳號授權</strong>
          <p style="margin:8px 0 0 0; color:#3c4043; line-height:1.7;">{app["license_warning"]}</p>
        </div>'''

    # 中英術語對照表
    terms = GLOSSARY.get(app['file'], [])
    gloss_html = ''
    if terms:
        rows = ''
        for zh, en, note in terms:
            mark = ''
            if note.startswith('★'):
                mark, note = ('<span title="核心功能" style="color:#b06000;">★</span> ', note[1:].strip())
            elif note.startswith('⚙'):
                mark, note = ('<span title="名稱須完全一致" style="color:#137333;">⚙</span> ', note[1:].strip())
            elif note.startswith('⚠️'):
                mark, note = ('<span style="color:#b3261e;">⚠️</span> ', note[2:].strip())
            rows += (f'<tr><td style="padding:8px 10px; border-top:1px solid #e8eaed;">{mark}{zh}</td>'
                     f'<td style="padding:8px 10px; border-top:1px solid #e8eaed; font-weight:600; color:#1557b0;">{en}</td>'
                     f'<td style="padding:8px 10px; border-top:1px solid #e8eaed; color:#5f6368; font-size:.88rem;">{note}</td></tr>')
        gloss_html = f'''
        <div style="background:#fff; border:1px solid #dadce0; border-radius:12px; padding:20px; margin:20px 0;">
          <h3 style="margin-top:0;">🔤 本篇功能術語中英對照</h3>
          <p style="font-size:.9rem; color:#5f6368; margin-bottom:12px;">
            Google 介面可切換語言，官方文件與國際研習場合也多用英文。
            操作時請順便記住右欄的英文名稱。
            <span style="color:#b06000; font-weight:700;">★</span> ＝核心功能
            <span style="color:#137333; font-weight:700;">⚙</span> ＝名稱須完全一致（系統逐字比對）
            <span style="color:#b3261e; font-weight:700;">⚠️</span> ＝容易混淆
          </p>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:.93rem;">
              <tr style="background:#f8f9fa;">
                <th style="text-align:left; padding:9px 10px; width:30%;">繁體中文介面</th>
                <th style="text-align:left; padding:9px 10px; width:32%;">English</th>
                <th style="text-align:left; padding:9px 10px;">備註</th>
              </tr>
              {rows}
            </table>
          </div>
        </div>'''

    n_word = ['零', '一', '二', '三', '四', '五', '六', '七', '八'][len(app['modules'])]

    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{app["title"]} (互動網頁版)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --primary-light: #e8f0fe;
      --secondary: #34a853;
      --text-main: #202124;
      --text-muted: #5f6368;
      --bg-body: #f8f9fa;
      --bg-card: #ffffff;
      --border: #dadce0;
      --shadow: 0 4px 16px rgba(0,0,0,0.06);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Google Sans', 'Noto Sans TC', sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
    }}

    header {{
      background: var(--primary);
      color: white;
      padding: 24px 32px;
      box-shadow: 0 4px 12px rgba(26,115,232,0.25);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .header-title h1 {{ font-size: 1.5rem; font-weight: 700; }}
    .header-title p {{ font-size: 0.9rem; opacity: 0.9; margin-top: 4px; }}

    .nav-links {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .nav-btn {{
      text-decoration: none;
      background: rgba(255,255,255,0.2);
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{ background: white; color: var(--primary); }}

    .app-layout {{
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
    }}

    @media (max-width: 900px) {{
      .app-layout {{ grid-template-columns: 1fr; }}
      .sidebar {{ position: static; }}
    }}

    .sidebar {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      height: fit-content;
      position: sticky;
      top: 100px;
    }}

    .sidebar-heading {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }}

    .menu-item {{
      display: block;
      width: 100%;
      text-align: left;
      border: none;
      background: transparent;
      padding: 12px 14px;
      border-radius: 8px;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      margin-bottom: 6px;
      transition: all 0.2s;
    }}

    .menu-item:hover {{ background: var(--bg-body); color: var(--primary); }}
    .menu-item.active {{ background: var(--primary-light); color: var(--primary); font-weight: 700; }}

    .content-area {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }}

    .module-card {{ display: none; }}
    .module-card.active {{ display: block; animation: fadeIn 0.3s ease-in-out; }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}

    h2 {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 16px; color: var(--primary-dark); }}
    h3 {{ font-size: 1.1rem; font-weight: 700; margin: 20px 0 10px 0; color: var(--text-main); }}
    p {{ margin-bottom: 14px; color: #3c4043; line-height: 1.7; }}

    .scenario-box {{
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
    }}

    .scenario-box strong {{ color: #b06000; }}

    .step-list {{
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin: 20px 0;
    }}

    .step-item {{
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    .step-item input[type="checkbox"] {{
      margin-top: 5px;
      width: 18px;
      height: 18px;
      cursor: pointer;
      flex-shrink: 0;
    }}

    code {{
      background: #f1f3f4;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 0.92em;
      color: #c5221f;
    }}

    .action-bar {{
      display: flex;
      gap: 12px;
      margin-top: 24px;
    }}

    .btn {{
      border: none;
      padding: 10px 20px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-primary {{ background: var(--primary); color: white; }}
    .btn-primary:hover {{ background: var(--primary-dark); }}

    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #323232;
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 0.9rem;
      display: none;
      z-index: 1000;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>{app["emoji"]} {app["title"]}</h1>
      <p>{app["subtitle"]}</p>
    </div>
    <div class="nav-links">
      <a href="study_guide_app.html" class="nav-btn">📖 回研習主講義</a>
      <a href="course_structure_map.html" class="nav-btn">🗺️ 課程結構對照</a>
    </div>
  </header>

  <div class="app-layout">

    <nav class="sidebar">
      <div class="sidebar-heading">實務演練章節選單</div>
{menu_html}    </nav>

    <main class="content-area">

      <!-- MODULE 0: OVERVIEW -->
      <div class="module-card active" id="module-0" style="display:block;">
        <span class="tag">研習簡介與教學策略</span>
        <h2>{app["name"]} 實務應用總覽</h2>
        <p>{app["overview_lead"]}</p>
{lic_html}
        <div style="background:#e8f0fe; border-radius:12px; padding:20px; margin:20px 0;">
          <h3 style="color:#1a73e8; margin-top:0;">💡 本章{n_word}大實務演練目標：</h3>
          <ul style="padding-left:20px; line-height:1.8; color:#3c4043;">
{goals_html}
          </ul>
        </div>

{gloss_html}
        <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:12px; padding:20px; margin:20px 0;">
          <h3 style="margin-top:0;">🧭 本篇會用到的練習方式：</h3>
          <ul style="padding-left:20px; line-height:1.8; color:#3c4043; list-style:none;">
{legend_html}
          </ul>
          <p style="margin:10px 0 0 0; font-size:0.9rem; color:#5f6368;">
            每則演練都先讀黃色的<strong>實務教學情境</strong>了解為什麼要做，再看彩色框的<strong>練習方式</strong>取得你的練習環境，
            最後照步驟清單逐項打勾。
          </p>
        </div>
      </div>

{cards_html}
    </main>
  </div>
{FOOTER}

  <div class="toast" id="toast">已複製操作步驟至剪貼簿！</div>

  <script>
    function showModule(idx) {{
      document.querySelectorAll('.menu-item').forEach((btn, i) => {{
        btn.classList.toggle('active', i === idx);
      }});
      document.querySelectorAll('.module-card').forEach((card, i) => {{
        card.style.display = (i === idx) ? 'block' : 'none';
        card.classList.toggle('active', i === idx);
      }});
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function copySteps(modId) {{
      const mod = document.getElementById(modId);
      const title = mod.querySelector('h2').innerText;
      const steps = Array.from(mod.querySelectorAll('.step-item label'))
        .map((l, i) => `${{i + 1}}. ${{l.innerText}}`)
        .join('\\n');

      const text = `【${{title}}】\\n${{steps}}`;
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.style.display = 'block';
        setTimeout(() => toast.style.display = 'none', 2500);
      }});
    }}
  </script>
</body>
</html>
'''


if __name__ == '__main__':
    for app in APPS:
        html = build_app(app)
        with open(os.path.join(ROOT, app['file']), 'w', encoding='utf-8') as f:
            f.write(html)
        types = ' '.join(sorted({m['practice']['type'] for m in app['modules']}))
        print(f"OK  {app['file']:32s} modules={len(app['modules'])}  types=[{types}]  size={len(html):,}")
    print('\n九篇工具講義已重建完成。')
