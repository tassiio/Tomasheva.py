salary = float(input("Enter your salary:\n"))
if salary < 10000:
    print("No tax.")
elif 50000 > salary >= 10000:
    print("Tax: ", 10000 * 0.13 + (salary - 10000) * 0.20)
else:
    print("Tax: ", 10000 * 0.13 + 40000 * 0.20 + 0.3 * (salary - 50000))
