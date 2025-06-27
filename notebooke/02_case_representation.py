# 02_case_representation.py
import re, os
import pandas as pd

def ekstrak_metadata(teks):
    no_perkara = re.search(r"(nomor|perkara)[\s:]*([\w/\-.]+)", teks, re.IGNORECASE)
    no_perkara = no_perkara.group(2) if no_perkara else ""
    pihak = re.search(r"antara\s+(.*?)\s+dengan\s+(.*?)\s", teks, re.IGNORECASE)
    pihak = f"{pihak.group(1)} vs {pihak.group(2)}" if pihak else ""
    pasal = re.findall(r"pasal\s+\d+[\s\S]{0,20}", teks, re.IGNORECASE)
    pasal = "; ".join(set(pasal)) if pasal else ""
    fakta = re.search(r"(menimbang|bahwa)[\s\S]{0,500}", teks.lower())
    fakta = fakta.group(0) if fakta else ""
    amar_patterns = [
        r"menolak", r"permohonan.*?ditolak", r"menghukum",
        r"mengabulkan", r"permohonan.*?dikabulkan", r"terkabulkan",
        r"diterima", r"terima"
    ]
    amar = ""
    for pattern in amar_patterns:
        match = re.search(pattern, teks.lower())
        if match:
            amar += match.group(0).strip() + " | "
    return no_perkara, pihak, pasal, fakta.strip(), amar.strip()

data = []
for file in os.listdir("data/raw"):
    if file.endswith(".txt"):
        with open(os.path.join("data/raw", file), encoding="utf-8") as f:
            teks = f.read()
            meta = ekstrak_metadata(teks)
            data.append({
                "case_id": file.replace(".txt", ""),
                "no_perkara": meta[0],
                "pihak": meta[1],
                "pasal": meta[2],
                "ringkasan_fakta": meta[3],
                "amar_patterns": meta[4],
                "isi_teks": teks
            })
df = pd.DataFrame(data)
df.to_csv("data/processed/cases.csv", index=False)