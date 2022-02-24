print("Введите три разных числа: ")
a = float(input())
b = float(input())
c = float(input())
# maximum = max(a, b, c)
# print("Максимальное из 3-ёх: ", maximum)
if a > b:
    max_num = a
else:
    max_num = b
if c > max_num:
    max_num = c
print("Максимальное из 3-ёх чисел: ", max_num)