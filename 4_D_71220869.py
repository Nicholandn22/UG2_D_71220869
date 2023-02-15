ttla = [""]
b = 1
ttlb = [""]
    
while b =='1':
    print('!! Selamat datang di H+ GYM')
    print('Silahkan pilih menu dibawah ini: ')
    print('1. Menambah data')
    print('2. Menampilkan data')
    print('3. Keluar')
    a = input(print('Silahkan masukkan pilihan yang Anda inginkan: '))
    if a == 1:
        a1 = str(input('Masukkan nama: '))
        a2 = str(input('DAILY'))
        print('Data sudah berhasil di tambahkan !')
        ttla.append(a1)
        ttlb.append(a2)
        b = 1

    elif a == 2:
        print('--------------------\n')
        print('Pelanggan ')
        c = len(ttla)
        print("Member :")
        d = len(ttlb)
        
    