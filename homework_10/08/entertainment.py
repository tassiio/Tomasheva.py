import random

sticks = int(input("Enter amount of sticks:\n"))
throws = int(input("Enter amount of throws:\n"))

row = ['|' for _ in range(sticks)]
print(''.join(row))

left_border = 0
right_border = 0
sticks_remain = 1
for i in range(throws):
    left_border = random.randrange(1, sticks + 1)
    while right_border < left_border:
        right_border = random.randrange(1, sticks + 1)
    print('Throw №', i + 1, ': left border - ', left_border, ", right - ", right_border)
    row = ['.' if right_border >= i + 1 >= left_border else row[i] for i in range(sticks)]
    sticks_remain = row.count('|')

print(''.join(row))
