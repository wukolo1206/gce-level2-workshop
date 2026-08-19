import shutil
import os

brain_dir = r"C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8"
target_dir = r"d:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images"

os.makedirs(target_dir, exist_ok=True)

img_map = {
    "gmail_auto_advance": "gmail_auto_advance.jpg",
    "calendar_appointments": "calendar_appointments.jpg",
    "smart_canvas_chips": "smart_canvas_chips.jpg",
    "sheets_data_query": "sheets_data_query.jpg"
}

for fname in os.listdir(brain_dir):
    for key, out_name in img_map.items():
        if fname.startswith(key) and fname.endswith(".jpg"):
            src_path = os.path.join(brain_dir, fname)
            dst_path = os.path.join(target_dir, out_name)
            shutil.copy2(src_path, dst_path)
            print(f"Copied {fname} -> {out_name}")

print("All images copied to target directory!")
