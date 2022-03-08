print("\n-----------------SESI 4-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

def kubus():
    print("\nMENGHITUNG VOLUME KUBUS\n")
    sisi =int(input("Masukkan sisi kubus = "))
    volume_kubus = sisi^3
    print("Sisi Kubus = ", sisi)
    print("Volume Kubus  = ", volume_kubus)
def balok():
    print("\nMENGHITUNG VOLUME BALOK\n")
    panjang =int(input("Masukkan panjang segi empat = "))
    lebar =int(input("Masukkan lebar segi empat = "))
    tinggi = int(input("Masukkan tinggi segi empat = "))
    volume_balok = panjang*lebar*tinggi
    print("Panjang balok = ", panjang)
    print("Lebar balok = ", lebar)
    print("Tinggi balok = ", tinggi)
    print("Volume Balok = ", volume_balok)
def bola():
    print("\nMENGHITUNG VOLUME BOLA\n")
    r =float(input("Masukkan jari jari bola = "))
    d=2*r
    volume_bola = (4/3)*(22/7)*(r^3)
    print("Panjang diameter bola = ", d)
    print("Volume bola = ", volume_bola)
