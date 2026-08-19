# -*- coding: utf-8 -*-
"""把 workshop_content.py 的 40 個演練匯出成純文字審查包，供外部 AI 交叉審查。"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workshop_content import APPS  # noqa: E402


def clean(t):
    t = re.sub(r'<br\s*/?>', ' ', t)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\s+', ' ', t).strip()


out = ['# 學員版實作演練 — 交叉審查包（第 2 版）\n',
       '> 2026-08-16 更新：已依第一輪審查回饋修正 26 條（介面名稱、步驟順序、前置條件）。\n',
       '> 範圍：10 篇工具講義、40 個實作演練，逐字對應學員看到的網頁內容。\n']
n = 0
for a in APPS:
    out.append('\n\n' + '=' * 72)
    out.append(f"\n## 【{a['name']}】{a['title']}\n檔案：{a['file']}\n")
    if a.get('license_warning'):
        out.append(f"\n※ 全篇授權提醒：{clean(a['license_warning'])}\n")
    for i, m in enumerate(a['modules'], 1):
        n += 1
        pr = m['practice']
        out.append(f"\n### 演練 {i}：{clean(m['title'])}　［全域編號 #{n}］")
        out.append(f"\n**功能說明**：{clean(m['intro'])}")
        out.append(f"\n**教學情境**：{clean(m['scenario'])}")
        out.append(f"\n**練習方式**：{pr['type']}")
        if pr['type'] == 'calendar':
            out.append(f"\n  預填活動：{pr['cal']['text']}　dates={pr['cal']['dates']}")
            out.append('\n  活動說明欄：\n  ' + pr['cal']['details'].replace('\n', '\n  '))
        for r in pr.get('roles', []):
            out.append(f"\n  - 角色分工：{clean(r)}")
        out.append(f"\n**指定任務**：{clean(pr['todo'])}")
        if pr.get('alt'):
            out.append(f"\n**替代練習**：{clean(pr['alt'])}")
        if pr.get('note'):
            out.append(f"\n**補充提醒**：{clean(pr['note'])}")
        out.append('\n**操作步驟**：')
        for si, s in enumerate(m['steps'], 1):
            out.append(f"\n  {si}. {clean(s)}")
        out.append('\n')

txt = '\n'.join(out)
p = os.path.join(ROOT, '學員版實作演練_審查包.md')
io.open(p, 'w', encoding='utf-8', newline='').write(txt)
print(f'審查包已更新：{n} 個演練，{len(txt):,} 字')
