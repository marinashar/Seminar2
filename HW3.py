# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

Number = int(input('Введите число n: '))

list = []
for e in range(1, Number + 1):
    list.append((1 + 1 / e)**e)
print(list)