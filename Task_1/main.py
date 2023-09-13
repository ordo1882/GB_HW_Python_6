# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Enter the first number: "))
d = int(input("Enter the step size: "))
n = int(input("Enter the steps number: "))

lst = [a1 if i == 0 else i * d + a1 for i in range(n)]

print("Arithmetical progression for your prompt is:", *lst)