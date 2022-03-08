print("-----------------looping (for)-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

l1=[1,2,3,4,5,6,7,8,9,10]
for i in l1:
    if i%2==0:
        print(i)
    else:
        print("ini angka ganjil")

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

example=["pen", "pineapple", "apa ya", "apa ya lagi"]
for item in example:
    print("i have a "+item)

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

for x in range(20, 30):
    print(x)

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

myString = "hacktivate"
for char in myString:
    print(char)

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

person = {'name' : 'aninditako', 'asal' : 'jogja'}

for key in person:
    print(key, ":", person[key])

print("---------------------------------------")
input("klik enter untuk ke menu selanjutya")
print("---------------------------------------\n")

blog_posts = {"Python" : ["Introduction to Python for Data Science", "Program Studi Independen", "Kampus Merdeka", "by Hacktivate Indonesia"]}

for category in blog_posts:
    print("ini adalah", category)
    for post in blog_posts[category]:
        print(post)