"""1.  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    *Пример:*
    - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    *Пример:*
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    *Пример:*
    - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    *Пример:*
    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    *Пример:*
    - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1,
 """
ls = [2, 3, 5, 9, 3]


def ls_sum(a):
    result = 0
    for i in range(len(a)):
        if i % 2 != 0:
            result += int(a[i])
    print(result)


ls_sum(ls)

##############################################


def multiply_sp(sp):
    if len(sp) % 2 != 0:
        print("Количество элементов списка не четное!")
        rz = int(len(sp) / 2) + 1
    else:
        rz = int(len(sp) / 2)

    mult = []
    for i in range(0, rz):
        mult.append(sp[i] * sp[len(sp) - 1 - i])
    return mult


if __name__ == "__main__":
    #    sp = [2, 3, 4, 5, 6]
    sp = [2, 3, 5, 6]
    print(sp, " => ", multiply_sp(sp))

################################################
n = [1.1, 1.2, 3.1, 10.01]


def average(n):
    max = 0
    min = 1  #
    for i in n:
        temp = round(i % 1, 3)  #
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    print(f"max {max} min {min}")
    res = max - min
    return res


print(average(n))
#################################################
a = [1.1, 1.2, 3.1, 5.10, 10.01]


def MaxMin(list):
    for i in range(len(list)):
        list[i] = list[i] % 1
    Result = round(max(list) - min(list), 3)
    return f"Разница между остатком дробей {round(max(list),3)} и {round(min(list),3)} = {Result}"


print(MaxMin(a))

###################################################
def DecToBin(n):
    lstBin = []
    while n > 0:
        lstBin.append(str(n % 2))
        n //= 2
    return "".join(lstBin[::-1])


print(DecToBin(6))

##################################################
a = int(input("Введите число -> "))

x = []
integer = []
result = []

x = list(str(a))[::-1]


while True:
    if a != 0:
        if a % 2 == 0:
            result.append(0)
            a = a // 2
        elif a % 2:
            result.append(1)
            a = a // 2
    else:
        result.reverse()
        print(result)
        break
input()
################################################
def fib(n):
    if n == 0:
        return 0
    elif n == -1:
        return -1
    else:
        return fib(n + 1) + fib(n + 2)


for i in range(-10, 1):

    print(f"{fib(i)}", end=" ")
##################################################
def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n - 2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list


x = fibo(10)
print(x)
