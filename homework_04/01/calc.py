points = int(input("Put the number of points: \n"))
if points / 1000 < 1:
    print("Your level is 1")
elif points / 1000 < 2.5:
    print("Your level is 2")
elif points / 1000 < 5:
    print("Your level is 3")
else:
    print("Your level is 4")
