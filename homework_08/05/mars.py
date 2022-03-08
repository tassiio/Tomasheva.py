# initial_position = []
print("Enter two coordinates of your machine (use Enter):")
# for i in range(0, 2):
# initial_position.append(int(input()))
initial_position = [8, 10]
initial_position = list(map(int, initial_position))
print("Your initial position:", initial_position)
boolean = 1
while boolean and initial_position[0] < 21 and initial_position[1] < 21:
    move = input("Where do you want to move? W - up, S - down, A - left, D - right, Stop - exit \n")
    if move == "W":
        if initial_position[1] < 20:
            initial_position[1] += 1
            print("You current position:", initial_position)
        else:
            print("You have reached the border of the area. Choose another option.")
    if move == "S":
        if initial_position[1] > 0:
            initial_position[1] -= 1
            print("You current position:", initial_position)
        else:
            print("You have reached the border of the area. Choose another option.")
    if move == "A":
        if initial_position[0] > 0:
            initial_position[0] -= 1
            print("You current position:", initial_position)
        else:
            print("You have reached the border of the area. Choose another option.")
    if move == "D":
        if initial_position[0] < 15:
            initial_position[0] += 1
            print("You current position:", initial_position)
        else:
            print("You have reached the border of the area. Choose another option.")
    if move == "Stop":
        boolean = 0
