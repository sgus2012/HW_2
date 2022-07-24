""" 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    1) с помощью математических формул нахождения корней квадратного уравнения
    
    2) с помощью дополнительных библиотек Python
    
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. """

# n = "12 45 85 676 215 456"

# list = [int(s) for s in n.split()]

# max = max(list)
# min = min(list)

# print(max)
# print(min)


a, b = 35.5, 40.1
i = min(a, b)
while True:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
""" from math import sqrt


A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B**2 - 4 * A * C

if D == 0:
    x = -B / (2 * A)
    print(f"Уравнение имеет один корень: {x}")
elif D > 0:
    x1 = (-B + sqrt(D)) / (2 * A)
    x2 = (-B - sqrt(D)) / (2 * A)
    print(f"Уравнение имеет два корня: x1={x1}; x2={x2}")
else:
    print("Уравнение не имеет вещественных корней") """

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

A = int(input("A="))
B = int(input("B="))


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    return gcd(b, a % b) if b != 0 else a


def lcm(a, b):
    return a / gcd(a, b) * b


print(lcm(A, B))
