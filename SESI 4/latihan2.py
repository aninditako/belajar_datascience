print("\n-----------------SESI 4-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

import PKG.bentuk3D as bentuk3D

ulang="Y"
while ulang=="Y" or ulang=="y":
    print("=========== BANGUN RUANG ===========")
    print("1. Kubus")
    print("2. Balok")
    print("3. Bola")
    pilih = int(input("Pilih menu : "))

    if pilih==1:
        bentuk3D.kubus()

    elif pilih==2:
        bentuk3D.balok()
    elif pilih==3:
        bentuk3D.bola()
    else:
        print("maaf pilihan anda tidak tersedia")
    ulang = input("\nIngin kembali ke menu? (y/n) : ")
else:
    print("-program selesai-\n")

