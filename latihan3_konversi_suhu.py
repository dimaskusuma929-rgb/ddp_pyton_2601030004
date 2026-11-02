# Program konversi suhu Celsius ke Fahrenheit dan Kelvin

# Input suhu Celsius dari pengguna
suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))

# Perhitungan konversi suhu
suhu_fahrenheit = (suhu_celsius * 9/5) + 32
suhu_kelvin = suhu_celsius + 273.15

# Menampilkan hasil konversi
print(f"Suhu dalam Fahrenheit : {suhu_fahrenheit} °F")
print(f"Suhu dalam Kelvin     : {suhu_kelvin} K")