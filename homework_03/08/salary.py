hours = float(input("Введите отработанные часы: \n"))
residue = float(input("Введите остаток по кредиту: \n"))
food = float(input("Введите траты на еду: \n"))
salary = 200 * hours / pow(2, 3) + hours
if salary >= residue + food:
    print("Часов хватает. Можно отдохнуть.")
else:
    print("Часов не хватает. Придётся работать!")
