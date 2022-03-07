scholarship = float(input("Enter the scholarship: \n"))
utility_bills = float(input("Enter utility bills: \n"))
summa = utility_bills
for i in range(2, 11):
    utility_bills *= 1.03
    summa += utility_bills
    # print(round(utility_bills, 3), round(summa, 3))
print("You need to ask parents for", round(summa - scholarship * 10, 3), "dollars")
