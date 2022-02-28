i = 1
counter_positive = 0
counter_negative = 0
while i != 0:
    print("Put your grade: ")
    i = int(input())
    if i > 0:
        counter_positive += 1
    elif i < 0:
        counter_negative += 1
print("There are", counter_positive, "positive grades.")
print("There are", counter_negative, "negative grades.")
