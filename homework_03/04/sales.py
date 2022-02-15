first = int(input("Введите стоимость 1-го стула: \n"))
# print(first)
second = int(input("Введите стоимость 2-го стула: \n"))
# print(second)
third = int(input("Введите стоимость 3-го стула: \n"))
# print(third)
Summ = first + second + third
if Summ > 10000:
    print("Сумма к оплате (с учётом 10-процентной скидки): \n", f'{Summ - 0.10 * Summ:.{1}f}')
else:
    print("Сумма к оплате:", Summ)
