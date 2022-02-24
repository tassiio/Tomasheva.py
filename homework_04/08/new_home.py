square = float(input("Enter the desired area of the flat (m^2):\n"))
price = float(input("How much does it cost? (millions)\n"))
if square >= 100:
    if price <= 10:
        print("The flat is OK.")
    else:
        print("It's too expensive. Find other variants.")
elif 100 > square >= 80:
    if price <= 7:
        print("The flat is OK.")
    else:
        print("It's too expensive. Find other variants.")
else:
    print("The flat is too small. Find other variants.")
