debtors = int(input("How many debtors are there? \n"))
summa = 0
debt = 0
for i in range(0, debtors, 5):
    print("The debtor number", i)
    debt = int(input("Enter you debt: "))
    summa += debt
print("The summa of the debt:", summa)
