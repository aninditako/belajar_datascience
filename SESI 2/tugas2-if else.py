print("------------conditionals (if else)-------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

number = int(input("masukan angka :  "))
if number%2==0:
    print("angka genap")
else:
    print("angka ganjil")

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

string = input("Input data string :  ") 
key = input("Input data yang akan dicari :  ")
if(key in string):                 
    print("ditemukan") 
else:
    print("tidak ditemukan \n")

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

name1=input("masukkan nama anda :  ")
course1=input("berapa banyak organisasi yang kamu ikuti :  ")

name2=input("masukkan nama anda :  ")
course2=input("berapa banyak organisasi yang kamu ikuti :  ")

name3=input("masukkan nama anda :  ")
course3=input("berapa banyak organisasi yang kamu ikuti :  ")

if float(course1)>float(course2) and float(course1)>float(course3):
    print(name1 + " yang paling aktif")
elif float(course2)>float(course1) and float(course2)>float(course3):
    print(name2 + " yang paling aktif")
elif float(course3)>float(course2) and float(course3)>float(course1):
    print(name3 + " yang paling aktif")

print("---------------------------------------")

