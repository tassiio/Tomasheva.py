summa = 0.0
for i in range(0, 12):
    summa += float(input("What is the salary for the month?\n"))
print("The average salary is", f'{summa / 12:.{1}f}')
