print("----------------looping (while)----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

a=1
while a<=10:
    print (a)
    a=a+1

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

x=25
y=50
while x<y:
    print(x)
    print("lebih kecil dari")
    x=x+5

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

x=0
while x<=5:
    if x<5:
        print('x adalah : ', x)
        print('x kurang dari 5, tambahkan 1 pada x')
        x=x+1
    elif x==5:
        print('x adalah : ', x)
        print('x sama dengan 5, tidak perlu menambahkan pada x')
        x=x+1

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

# x=0
# people=[]
# while x<5:
#     person = input("masukkan nama : ")
#     people.append(person)
#     x+=1
# print(people)

x=0
people=[]
while len(people)<5:
    person = input("masukkan nama : ")
    people.append(person)
print(people)

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

import random
x=random.randint(0,10)
print("x=?")
print("clue: angka diantara 0 sampai 10")
tebak=int(input("angka x adalah : "))
while True:
    if tebak == x:
        break
    else:
        tebak=int(input("yok bisa yok, coba lagi : "))
print("yey benar, angkanya adalah", x)



    