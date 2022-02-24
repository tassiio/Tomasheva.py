place = int(input("Enter your place on the list:\n"))
if place < 11:
    print("Congratulations! You have entered the university!")
    points = int(input("Enter the number of points you have:\n"))
    if points >= 290:
        print("Congratulations! You will receive a scholarship!")
    else:
        print("Unfortunately, your points are too low for a scholarship.")
else:
    print("Unfortunately, you haven't entered the university.")
