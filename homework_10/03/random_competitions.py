import random

first_points = [round(random.random() * (10 - 5) + 5, 2) for _ in range(20)]
second_points = [round(random.random() * (10 - 5) + 5, 2) for _ in range(20)]

print(first_points)
print(second_points)

winners = [max(first_points[i], second_points[i]) for i in range(20)]
print(winners)
