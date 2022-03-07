disturbances = 0
for i in range(30, 36):
    print("How many people are in the", i, "sector?")
    people = int(input())
    if people <= 10:
        print("Everything is okay!")
    else:
        print("There are too many people!")
        disturbances += 1
print("The amount of disturbances is", disturbances)
