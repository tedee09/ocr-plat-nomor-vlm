#  OCR Plat Nomor dengan Vision Language Model (LLaVA v1.5)

##  Deskripsi
Proyek ini melakukan Optical Character Recognition (OCR) pada gambar plat nomor kendaraan menggunakan model LLaVA v1.5 yang dijalankan secara lokal dengan LM Studio. Model ini menerima gambar dan prompt untuk mengenali isi plat.

##  Struktur Proyek
```
aas/
├── test/ # Folder gambar plat nomor
├── labels.csv # Label ground truth plat
├── ocr_predict.py # Script untuk memprediksi isi plat nomor
├── analisis_hasil.py # Script untuk mengevaluasi hasil (CER)
├── hasil_prediksi.csv # Output akhir prediksi
```

##  Tools yang Digunakan
- LM Studio (GUI + API server untuk LLaVA)
- Python 3.11
- Libraries: `requests`, `pandas`, `Levenshtein`

## ▶️ Cara Menjalankan

### 1. Aktifkan Model LLaVA di LM Studio

- Buka **LM Studio**.
- Klik tab **"Developer"** di sisi kiri.
- Aktifkan opsi **"Serve on Local Network"**.
- Catat port server (contoh: `1234`).
- Klik tab **"Status"**, pastikan status model **Running**.
- Buka browser dan kunjungi:

```
http://localhost:1234/v1/models
```

Jika model aktif, akan muncul respon seperti ini:
```
{
  "data": [
    {
      "id": "llava-v1.5-7b",
      "object": "model",
      "owned_by": "organization_owner"
    },
    {
      "id": "text-embedding-nomic-embed-text-v1.5",
      "object": "model",
      "owned_by": "organization_owner"
    }
  ],
  "object": "list"
}
````

### 2. Jalankan Prediksi Plat Nomor
Buka terminal dan arahkan ke folder proyek:
```
cd path/ke/folder/aas
python ocr_predict.py
````

### 3. Evaluasi Hasil CER
Setelah prediksi selesai, jalankan evaluasi:
```
python analisis_hasil.py
```
Hasil akhir akan tersimpan dalam file hasil_prediksi.csv, dan output analisis akan tampil di terminal (jumlah prediksi berdasarkan kategori dan rata-rata CER).

##  Evaluasi Hasil
- Gambar diuji: **168**
- Rata-rata CER: **~0.586**
- Distribusi hasil:
  -  Akurat: 6 gambar
  -  Lumayan: 91 gambar
  -  Gagal: 71 gambar

## 📖 Formula CER
CER = (S + D + I) / N
S = substitusi
D = deletion
I = insertion
N = jumlah karakter ground truth