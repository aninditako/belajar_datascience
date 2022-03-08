print("\n-----------------SESI 4-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

import PKG.bentuk2D as bentuk2D

ulang="Y"
while ulang=="Y" or ulang=="y":
    print("=========== BANGUN DATAR ===========")
    print("1. Segitiga")
    print("2. Persegi")
    print("3. Lingkaran")
    pilih = int(input("Pilih menu : "))

    if pilih==1:
        bentuk2D.segitiga()

    elif pilih==2:
        bentuk2D.persegi()
    elif pilih==3:
        bentuk2D.lingkaran()
    else:
        print("maaf pilihan anda tidak tersedia")
    ulang = input("\nIngin kembali ke menu? (y/n) : ")
else:
    print("-program selesai-\n")

