a = str(input('Masukkan Nomor Telepon : '))
if a[:4] == "0816":
    print("Anda menggunakan operator Indosat")
    b=int(a)
    if b % 2 == 0:
        print('Nomor anda berakhiran genap')
    else :
        print('Nomor anda berakhiran ganjil')
elif a[:4] == "0814":
    print("Anda menggunakan operator Telkomsel")
    b=int(a)
    if b % 2 == 0:
        print('Nomor anda berakhiran genap')
    else :
        print('Nomor anda berakhiran ganjil')
else : 
    print('Operator anda tidak diketahhui')
    b=int(a)
    if b % 2 == 0:
        print('Nomor anda berakhiran genap')
    else :
        print('Nomor anda berakhiran ganjil')


