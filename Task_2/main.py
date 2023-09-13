# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

MIN = int(input("Enter the lowest limit: "))
MAX = int(input("Enter the highest limit: "))

lst = [random.randint(-20, 20) for _ in range(20)]

print(*lst)

print("Index range is:")

lst = [print(i, end=' ') for i in range(len(lst)) if MIN <= lst[i] <= MAX]