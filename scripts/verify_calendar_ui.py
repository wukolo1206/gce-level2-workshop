# -*- coding: utf-8 -*-
"""
唯讀驗證：確認講義中 Calendar 演練的按鈕名稱與實際介面一致。

流程：開一個真實 Chrome 視窗 ➔ 使用者手動登入 Google ➔ 腳本自動開啟講義中的
活動預填網址 ➔ 讀取說明欄工具列與邀請對象權限區塊的實際按鈕名稱 ➔ 截圖。

安全性：全程唯讀。只開啟「尚未儲存的活動草稿」並讀取畫面文字，
不點選儲存、不建立活動、不修改任何既有資料。
"""
import io
import os
import re
import sys
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = r'C:\Users\wu\AppData\Local\Temp\claude\d----ai-----\5d032a5f-856d-4c15-ae2f-c291fff9b6f9\scratchpad'
PROFILE = os.path.join(SCRATCH, 'chrome_profile_verify')
SHOTS = os.path.join(SCRATCH, 'ui_check')
os.makedirs(SHOTS, exist_ok=True)

# 從已產生的講義中撈出 Calendar 預填網址（確保驗的就是學員會點到的那條）
html = io.open(os.path.join(ROOT, 'calendar_workshop_app.html'), encoding='utf-8').read()
CAL_URLS = [u.replace('&amp;', '&') for u in re.findall(r'href="(https://calendar\.google\.com[^"]+)"', html)]
NAMES = ['演練二_Meet直播', '演練三_邀請對象權限', '演練四_建立會議記錄']

result = {'urls_checked': len(CAL_URLS), 'findings': []}


def dump(pg, tag):
    """讀取畫面上所有按鈕的可及性名稱，找出講義提到的關鍵字。"""
    labels = []
    for sel in ['button', '[role=button]', '[role=checkbox]', 'input[type=checkbox]']:
        for el in pg.locator(sel).all()[:400]:
            try:
                nm = (el.get_attribute('aria-label') or el.get_attribute('data-tooltip')
                      or el.get_attribute('title') or el.inner_text() or '').strip()
            except Exception:
                continue
            if nm and nm not in labels:
                labels.append(nm)
    keys = ['會議記錄', '會議紀錄', 'meeting note', '邀請其他使用者', '查看邀請對象名單',
            '修改活動', 'Google Meet', '串流直播', '直播', '通知', '更多選項']
    hit = {k: [l for l in labels if k.lower() in l.lower()] for k in keys}
    return labels, {k: v for k, v in hit.items() if v}


with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        PROFILE, channel='chrome', headless=False,
        viewport={'width': 1400, 'height': 950},
        args=['--start-maximized'])
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()

    pg.goto('https://calendar.google.com/')
    print('>>> 請在剛開啟的 Chrome 視窗中登入你的 Google 帳號（最多等 8 分鐘）…')

    logged = False
    for _ in range(96):  # 8 分鐘
        time.sleep(5)
        if 'calendar.google.com' in pg.url and 'accounts.google.com' not in pg.url:
            try:
                if pg.locator('[role=grid], [data-viewkey]').count() > 0:
                    logged = True
                    break
            except Exception:
                pass
    if not logged:
        print('!!! 逾時未偵測到登入完成，中止（沒有動到任何資料）')
        ctx.close()
        sys.exit(1)

    print('>>> 偵測到已登入，開始唯讀檢查…\n')
    for name, url in zip(NAMES, CAL_URLS):
        print(f'=== {name} ===')
        pg.goto(url)
        pg.wait_for_timeout(4500)

        # 1) 快速編輯面板
        labels, hit = dump(pg, name)
        pg.screenshot(path=os.path.join(SHOTS, name + '_1快速面板.png'))
        for k, v in hit.items():
            print(f'   [快速面板] 命中「{k}」: {v[:3]}')

        # 2) 進入「更多選項」完整編輯頁（僅瀏覽，不儲存）
        labels2, hit2 = {}, {}
        try:
            more = pg.locator('text=更多選項').first
            if more.count() == 0:
                more = pg.locator('[aria-label*="更多選項"], [aria-label*="More options"]').first
            more.click(timeout=5000)
            pg.wait_for_timeout(5000)
            labels2, hit2 = dump(pg, name + '_full')
            pg.screenshot(path=os.path.join(SHOTS, name + '_2完整編輯頁.png'), full_page=True)
            for k, v in hit2.items():
                print(f'   [完整頁]   命中「{k}」: {v[:3]}')
        except Exception as e:
            print('   （無法進入完整編輯頁：', str(e)[:60], '）')

        if not hit and not hit2:
            print('   ⚠️ 未命中任何關鍵字，請看截圖判讀')
        result['findings'].append({'module': name, 'quick': hit, 'full': hit2})
        print()

    io.open(os.path.join(SHOTS, 'result.json'), 'w', encoding='utf-8').write(
        json.dumps(result, ensure_ascii=False, indent=2))
    print('>>> 檢查完成，截圖存於：', SHOTS)
    print('>>> 視窗保留 60 秒供你自行確認，之後自動關閉（未儲存任何活動）。')
    time.sleep(60)
    ctx.close()
