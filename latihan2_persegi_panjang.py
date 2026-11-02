# Program menghitung luas dan keliling persegi panjang

# =====================================================================
# TRACE TABLE
# =====================================================================
# Contoh Input: panjang_sisi = 10.0, lebar_sisi = 5.0
# ---------------------------------------------------------------------
# Baris Kode                             | Variabel     | Nilai
# ---------------------------------------------------------------------
# panjang_sisi = float(input(...))       | panjang_sisi | 10.0
# lebar_sisi = float(input(...))         | lebar_sisi   | 5.0
# luas_ruang = panjang_sisi * lebar_sisi | luas_ruang   | 50.0
# keliling_ruang = 2 * (panjang + lebar) | keliling     | 30.0
# print(...)                             | Output       | 50.0 dan 30.0
# =====================================================================

# Input dari pengguna
panjang_sisi = float(input("Masukkan panjang: "))
lebar_sisi = float(input("Masukkan lebar: "))

# Hitung luas dan keliling
luas_ruang = panjang_sisi * lebar_sisi
keliling_ruang = 2 * (panjang_sisi + lebar_sisi)

# Menampilkan hasil perhitungan
print(f"Luas persegi panjang    : {luas_ruang}")
print(f"Keliling persegi panjang: {keliling_ruang}")