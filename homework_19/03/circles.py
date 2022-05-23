from circle_cl import Circle

circle_one = Circle()
circle_two = Circle(1, 2, 3)

print(circle_one.circle_area(), circle_two.circle_area())
print(circle_one.circle_perimeter(), circle_two.circle_perimeter())
circle_one.circle_scale(2)
circle_two.circle_scale(1/3)
print(circle_one.radius, circle_two.radius)

if circle_one.circle_intersection(circle_two.get_center()[0], circle_two.get_center()[1], circle_two.radius):
    print('Intersect.')
else:
    print("Don't intersect.")
