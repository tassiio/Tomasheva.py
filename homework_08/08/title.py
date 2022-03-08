length = int(input("Enter the length of the title:\n"))
excl_marks = int(input("Enter the number of exclamation marks:\n"))
len_2 = int((length - excl_marks)/2)
if length % 2 == excl_marks % 2:
    for i in range(len_2):
        print("~", end='')
    for i in range(excl_marks):
        print("!", end='')
    for i in range(len_2):
        print("~", end='')
else:
    for i in range(len_2 + 1):
        print("~", end='')
    for i in range(excl_marks):
        print("!", end='')
    for i in range(len_2):
        print("~", end='')
