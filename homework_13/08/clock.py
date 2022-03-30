angle = float(input("Enter the clockwise rotation angle (grad): "))
hours = angle * 12.0 / 360.0
# print("Hours = ", int(hours))
minutes = (hours - int(hours)) * 60
# print("Minutes = ", minutes)
print("The angle of rotation of minute hand:", minutes * 360 / 60)
