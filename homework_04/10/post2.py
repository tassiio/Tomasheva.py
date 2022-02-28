time = int(input("Enter an hour of visiting the post office:\n"))
if 10 <= time < 12 or 14 <= time < 15 or 18 <= time < 20:
    print("Sorry, we are busy. You can't receive the package right now.")
else:
    print("You can receive your package.")
