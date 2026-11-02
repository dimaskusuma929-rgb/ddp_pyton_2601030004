# Program menghitung total belanja dengan PPN 11%

# Input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja (Rp): "))

# Perhitungan PPN 11% dan total bayar
nilai_ppn = total_belanja * 0.11
total_bayar = total_belanja + nilai_ppn

# Menampilkan rincian total pembayaran
print(f"Total Belanja : Rp {total_belanja:,.2f}")
print(f"PPN (11%)     : Rp {nilai_ppn:,.2f}")
print(f"Total Bayar   : Rp {total_bayar:,.2f}")