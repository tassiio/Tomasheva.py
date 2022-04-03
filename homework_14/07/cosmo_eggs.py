danger_level = 1
while danger_level >= 1 or danger_level < 0:
    danger_level = float(input("Enter the accepted level of danger: "))


def danger(x):
    return pow(x, 3) - 3 * pow(x, 2) - 12 * x + 10


left_border = 0.0
right_border = 4.0

while right_border - left_border >= danger_level:
    depth = (right_border + left_border) / 2
    if danger(left_border) * danger(depth) < 0:
        right_border = depth
    else:
        left_border = depth

print(f'Approximate depth of the safe location: {(right_border + left_border) / 2:.9f}')
# print("For this level it is impossible to pick up the depth.")
