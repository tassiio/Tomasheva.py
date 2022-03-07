a = int(input("The beginning of the segment: \n"))
b = int(input("The end of the segment: \n"))

summa = 0
amount = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        summa += i
        amount += 1
print("The average is", f'{summa / amount:.{2}f}')
