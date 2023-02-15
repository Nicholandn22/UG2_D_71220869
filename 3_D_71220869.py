print('Masukkan Brand apa saja yang hendak dibeli (pisahkan dengan koma): H&M, Fendi, LV, Dior')
a = int(input('Berapa harga barang H&M ?:'))

if a >= 25000000:
    b = a - (a /4)
    c0 = a /4
    print('harga H&M \t Rp. ',a,'\t Diskon Rp. ',c0)
elif a >= 10000000:
    b = a - (a * 0.1)
    c0 = a * 0.1
    print('harga H&M \t Rp. ',a,'\t Diskon Rp. ',c0)
else :
    c0 = 0
    b = 0
    print('harga H&M \t Rp. ',a,'\t Diskon Rp. 0')


a1 = int(input('Berapa harga barang Fendi ?:'))
if a1 >= 25000000:
    b1 = a1 - (a /4)
    c4 = a1 /4
    print('harga Fendi \t Rp. ',a1,'\t Diskon Rp. ',c4)
elif a1 >= 10000000:
    b1 = a1 - (a1 * 0.1)
    c4 = a1 * 0.1
    print('harga Fendi \t Rp. ',a1,'\t Diskon Rp. ',c4)
else :
    print('harga Fendi \t Rp. ',a1,'\t Diskon Rp. 0')
    c4 = 0
    b1 = 0


a2 = int(input('Berapa harga barang LV ?:'))

if a2 >= 25000000:
    b2 = a2 - (a2 /4)
    c2 = a2 /4
    print('harga LV \t Rp. ',a2,'\t Diskon Rp. ',c2)
elif a2 >= 10000000:
    b2 = a2 - (a2 * 0.1)
    c2 = a2 * 0.1
    print('harga LV \t Rp. ',a2,'\t Diskon Rp. ',c2)
else :
    print('harga LV \t Rp. ',a2,'\t Diskon Rp. 0')
    c2 = 0
    b2 = 0

a3 = int(input('Berapa harga barang Dior ?:'))

if a3 >= 25000000:
    b3 = a3 - (a3 /4)
    c3 = a3 /4
    print('harga Dior \t Rp. ',a3,'\t Diskon Rp. ',c3)
elif a3 >= 10000000:
    b3 = a3 - (a3 * 0.1)
    c3 = a3 * 0.1
    print('harga Dior \t Rp. ',a3,'\t Diskon Rp. ',c3)
else :
    print('harga Dior \t Rp. ',a3,'\t Diskon Rp. 0')
    c3 = 0
    b3 = 0

ttldskn = c0 + c4 + c2 + c3
print('Total diskon yang anda dapatkan adalah sebesar Rp. ',ttldskn)
Ttluag = b + b1 + b2 + b3
hasil = Ttluag - 10000000
print('Total uang yang harus anda bayarkan adalah: Rp. ',hasil)