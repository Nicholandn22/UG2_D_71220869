print('=============== MAKANAN ===============')
print('1. Telur Bakar          : Rp 7.000')
print('2. Lele Terbang Mas Bhe : Rp 10.000')
print('3. Es Coklat Lempu      : Rp 5.000')
print('4. Es Doger Langensari  : Rp 13.000')
print()

print('=============== PESANAN ===============')
a = int(input('Telur Bakar  : '))
ha = 7000
b = int(input('Lele Terbang : '))
hb = 10000
c = int(input('Es Coklat    : '))
hc = 5000
d = int(input('Es Doger     : '))
hd = 13000
print()
print('=============== TOTAL ===============')
ta = a * ha
tb = b * hb
tc = c * hc
td = d * hd

print(f'Total TELUR BAKAR x {a}\t: Rp ',ta)
print(f'Total LELE TERBANG x {b}\t: Rp ',tb)
print(f'Total ES COKLAT x {a}\t: Rp ',tb)
print(f'Total ES DOGER x {a}\t: Rp ',td)
total = ta + tb + tc + td
print('Jumlah total biaya yang harus di bayar adalah Rp ',total)







