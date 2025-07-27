import pandas as pd

# Baca file hasil prediksi
df = pd.read_csv("hasil_prediksi.csv")

# Fungsi untuk mengelompokkan hasil berdasarkan CER
def klasifikasi_cer(cer):
    if cer <= 0.3:
        return "Akurat"
    elif cer <= 0.6:
        return "Lumayan"
    else:
        return "Gagal"

# Tambahkan kolom kategori ke dataframe
df["kategori"] = df["CER_score"].apply(klasifikasi_cer)

# Tampilkan hasil klasifikasi
print("Jumlah prediksi per kategori:")
print(df["kategori"].value_counts())
print()

# Tampilkan rata-rata CER
print(f"Rata-rata CER: {df['CER_score'].mean():.3f}")
