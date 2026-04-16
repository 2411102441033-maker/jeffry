# hitung harga
def hitung(a, b):
    c = a - (a * (b / 100))
    return c

# cek murah atau tidak
def cek(x):
    if x < 50000:
        return "Murah"
    else:
        return "Mahal"

# main
h = 100000
d = 20
hf = hitung(h, d)
status = cek(hf)
print("Harga akhir:", hf)
print("Status:", status)

# duplikasi logika lagi di bawah
h2 = 200000
d2 = 30
hf2 = hitung(h2, d2)
status2 = cek(hf2)
print("Harga akhir 2:", hf2)
print("Status 2:", status2)