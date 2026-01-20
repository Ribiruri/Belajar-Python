# Day 2: 30 Days of python programming
first_name = 'Akito'
last_name = 'Ryusei'
full_name = 'Akito Ryusei'
country = 'Indonesia'
city = 'Swiss Van Java'
age = 17
year = 2026
is_married = False
is_true = True
is_light_on = True
a, b, c = 1, 2, 3

# checking data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

# using len to find the length of my first name
convert1 = len(first_name)
convert2 = len(last_name)

print(len(first_name))
print(len(last_name))
print(convert1 > convert2)

# declare number
num_one = 5
num_two = 4

print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)
print(num_two % num_one)
print(num_one ** num_two)
print(num_one // num_two)

# the circle thing
r = 30
phi = 3.14
area_of_circle = phi * r**2
circum_of_circle = 2 * phi * r

ruser = int(input("Masukan angka radius : "))
aocm = phi * ruser**2
print(aocm)

# input user
nama_depan = input('Masukan nama depan anda : ')
nama_belakang = input('Masukan nama belakang anda : ')
negara = input('Anda tinggal dinegara mana : ')
umur = input('Masukan umur anda : ')
print(nama_depan,' ', nama_belakang, ' ', negara, ' ', umur)

help('keywords')
