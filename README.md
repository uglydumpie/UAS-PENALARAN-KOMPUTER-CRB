# UAS-PENALARAN-KOMPUTER-CRB

# Case-Based Reasoning (CBR) - Klasifikasi Putusan Mahkamah Agung

Tugas UAS Penalaran Komputer 2024/2025: Membangun sistem Case-Based Reasoning (CBR) untuk klasifikasi dan prediksi hasil putusan Mahkamah Agung berdasarkan kasus-kasus sebelumnya.

## Struktur Folder

- `/data/raw/` → Berisi file putusan mentah (.txt) hasil ekstraksi PDF
- `/data/processed/` → Berisi file CSV hasil ekstraksi metadata kasus
- `/notebooks/` → Berisi Jupyter notebook tahap demi tahap
- `README.md` → Penjelasan instalasi dan cara pakai
- `requirements.txt` → Dependensi proyek (lihat bagian bawah)

## Cara Instalasi & Menjalankan

1. **Instalasi Dependensi**
```bash
pip install -r requirements.txt
```

2. **Letakkan File Putusan**
Letakkan semua file `.txt` hasil ekstraksi di:
```
/data/raw/
├── case_001.txt
├── case_002.txt
└── ...
```

3. **Jalankan Notebook Secara Berurutan**
- `01_extraction.ipynb` → Konversi PDF & pembersihan teks
- `02_representation.ipynb` → Ekstraksi metadata dan struktur data ke CSV
- `03_retrieval.ipynb` → TF-IDF + cosine similarity + klasifikasi SVM/NB
- `04_predict.ipynb` → Prediksi amar dari kasus baru (menggunakan voting)

## Contoh Perintah

```python
# Menemukan 5 kasus paling mirip
retrieve("Penggugat menuntut ganti rugi karena wanprestasi", k=5)

# Prediksi hasil putusan
predict_outcome("Tergugat tidak memenuhi isi perjanjian sesuai kontrak")
```

## Identitas

- Nama: **[IDA KHOIRIYAH]**
- NIM: **[202210370311162]**
- Prodi: Teknik Informatika, Universitas Muhammadiyah Malang
