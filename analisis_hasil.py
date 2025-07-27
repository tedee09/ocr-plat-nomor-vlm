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

# Contoh hasil prediksi sukses dan gagal
contoh_akurat = df[df["kategori"] == "Akurat"].iloc[0]
contoh_gagal = df[df["kategori"] == "Gagal"].iloc[0]

print("\n📌 Contoh Prediksi Akurat:")
print(f"Image         : {contoh_akurat['image']}")
print(f"Ground Truth  : {contoh_akurat['ground_truth']}")
print(f"Prediction    : {contoh_akurat['prediction']}")
print(f"CER Score     : {contoh_akurat['CER_score']:.3f}")

print("\n📌 Contoh Prediksi Gagal:")
print(f"Image         : {contoh_gagal['image']}")
print(f"Ground Truth  : {contoh_gagal['ground_truth']}")
print(f"Prediction    : {contoh_gagal['prediction']}")
print(f"CER Score     : {contoh_gagal['CER_score']:.3f}")
