length = float(input("Enter the length of the letter: \n"))
width = length
amount = 0
while length > 12:
    length = length / 2
    amount += 2
    width = length
print("Amount:", amount)


# length = float(input("Enter the length of the letter: \n"))
# length_max = length
# Length_min = length
# i = 0
# while length_max > 12:
#   length_max /= 2
#   length_min, length_max = min(length_min, length_max), max(length_min, length_max)
#   i += 1
