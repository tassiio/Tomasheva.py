people = int(input("Enter the amount of people:\n"))
number = int(input("What's number in the rhyme?\n"))

circle = []
for i in range(people):
    circle.append(i + 1)
circle = list(map(int, circle))
print(circle)
start = 0
while len(circle) > 1:

    print("Now playing:", circle)
    dropout = number % len(circle) - 1 + start
    print("Start: ", circle[start])
    print("Dropout: ", circle[dropout])
    del circle[dropout]
# [circle[i] for i in range(length) if i != dropout]
    if len(circle) != 1:
        print("Game is going on for", circle)
    if dropout == len(circle):
        start = 0
    else:
        start = dropout
print("The winner is", circle)
