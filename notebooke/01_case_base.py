# 01_case_base.py
from pdfminer.high_level import extract_text
import os, re

def bersihkan_teks(teks):
    teks = teks.lower()
    teks = re.sub(r'\s+', ' ', teks)
    teks = re.sub(r'page \d+|halaman \d+', '', teks)
    teks = re.sub(r'[^\w\s]', '', teks)
    return teks.strip()

folder_pdf = "pdf_putusan"
folder_txt = "data/raw"
os.makedirs(folder_txt, exist_ok=True)

for i, filename in enumerate(sorted(os.listdir(folder_pdf))):
    if filename.endswith(".pdf"):
        path = os.path.join(folder_pdf, filename)
        try:
            text = extract_text(path)
            bersih = bersihkan_teks(text)
            with open(f"{folder_txt}/case_{i+1:03d}.txt", "w", encoding="utf-8") as f:
                f.write(bersih)
        except Exception as e:
            print(f"Gagal baca {filename}: {e}")