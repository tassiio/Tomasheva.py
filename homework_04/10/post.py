time = int(input("Enter an hour of visiting the post office:\n"))
if 8 <= time < 10 or 12 <= time < 14 or 15 <= time < 18 or 20 <= time < 22:
    print("You can receive your package.")
else:
    print("Sorry, we are busy. You can't receive the package right now.")