first = int(input("Put the first number: \n"))
second = int(input("Put the second number: \n"))
first_dec = first//10 % 10
second_dec = second//10 % 10
first_un = first - first//10 * 10
second_un = second - second//10 * 10
print(first_dec * 10 + first_un + second_dec * 10 + second_un)
