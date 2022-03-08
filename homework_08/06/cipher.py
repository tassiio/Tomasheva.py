string = input("Enter the message:\n")
counter = 1
maxx = 0
for i in range(1, len(string)):
    if string[i] == string[i-1] == "s":
        counter += 1
        if maxx < counter:
            maxx = counter
    else:
        counter = 1
print("Max 's' - substring has ", maxx)
