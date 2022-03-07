N = int(input("Enter N: \n"))
summa = 0
for i in range(0, N + 1):
    summa += pow(-1, i) * pow(2, -i)
print("Sum of the row:", summa)
