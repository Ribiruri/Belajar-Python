# day 3 of learning how to code in python
age = int(17)
height = float(5.7)
complex = complex(1+2j)

# script that enter the base and height to calculate the area of the triangle
baset = int(input("Enter base : "))
heightt = int(input("Enter the height : "))
ct = 0.5 * baset * heightt
print (ct)

# script that enter the a b c side to calculate the perimeter of triangle
a = int(input("Enter the a value : "))
b = int(input("Enter the b value : "))
c = int(input("Enter the c value : "))
d = a + b + c
print (d)

# script that enter the value of lenght and width to calculate the area of rectangle
length = int(input("Enter the length value : "))
width = int(input("Enter the width value : "))
cr = 2 * length + 2 * width
print (cr)

# script that enter the value of radius circle and calculate the area and circumference circle
radius = float(input("Enter the radius value : "))
pi = float(3.14)
cac = pi * radius * radius
ccc = 2 * pi * radius
print (cac)
print (ccc)

# Mendefinisikan komponen dari persamaan y = mx + c
# Untuk persamaan y = 2x - 2
m = 2  # Ini adalah slope (gradien)
c = -2 # Ini adalah konstanta (y-intercept)

print(f"Persamaan: y = {m}x + ({c})")
print("-" * 30)

# 1. Menentukan Slope
slope = m
print(f"1. Slope (Kemiringan): {slope}")

# 2. Menentukan Y-Intercept
# Terjadi saat x = 0, sehingga y = m(0) + c
y_intercept = c
print(f"2. Y-Intercept: (0, {y_intercept})")

# 3. Menghitung X-Intercept
# Terjadi saat y = 0, maka: 0 = mx + c
# Pindah ruas: -c = mx  =>  x = -c / m
x_intercept = -c / m
print(f"3. X-Intercept: ({x_intercept}, 0)")
