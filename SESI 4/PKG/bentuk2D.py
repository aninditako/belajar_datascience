print("\n-----------------SESI 4-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

def segitiga():
    print("\nMENGHITUNG KELILING DAN ALAS SEGITIGA\n")
    alas =int(input("Masukkan sisi alas segi tiga = "))
    tinggi =int(input("Masukkan tinggi segi tiga = "))
    keliling_segitiga = 3*alas
    luas_segitiga = alas*tinggi/2
    print("Alas segi tiga = ", alas)
    print("Tinggi segi tiga  = ", tinggi)
    print("Keliling segi tiga  = ", keliling_segitiga)
    print("Luas segi tiga  = ", luas_segitiga)
def persegi():
    print("\nMENGHITUNG KELILING DAN ALAS PERSEGI\n")
    panjang =int(input("Masukkan panjang segi empat = "))
    lebar =int(input("Masukkan lebar segi empat = "))
    keliling_segiempat = 2*panjang + 2*lebar
    luas_segiempat = panjang*lebar
    print("Panjang segi empat = ", panjang)
    print("Lebar segi empat = ", lebar)
    print("Keliling segi empat = ", keliling_segiempat)
    print("Luas segi empat = ", luas_segiempat)
def lingkaran():
    print("\nMENGHITUNG KELILING DAN ALAS LINGKARAN\n")
    r =float(input("Masukkan jari jari lingkaran = "))
    d=2*r
    keliling_lingkaran = 22/7*d
    luas_lingkaran = 22/7*r*r
    print("Panjang diameter lingkaran = ", d)
    print("Keliling lingkaran = ", keliling_lingkaran)
    print("Luas lingkaran = ", luas_lingkaran)
