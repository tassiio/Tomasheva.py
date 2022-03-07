massive = input("Put 10 integer numbers: ").split()
amount = 0
for i in range(len(massive)):
    # massive[i] = str(massive[i])
    if int(massive[i]) > 0 and int(massive[i]) % 2 == 0:
        # print(i+1, ":", massive[i], "is positive and even")
        amount += 1
print("There are", amount, "positive and even numbers in your massive.")
