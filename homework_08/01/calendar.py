the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = input("Enter any day of the week: \n")
for i in range(len(the_week)):
    if the_week[i] == day:
        print("The number of the day:", i + 1)
        break
