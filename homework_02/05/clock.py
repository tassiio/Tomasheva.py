minutes = int(input("Put amount of minutes: \n"))
hours = minutes//60
minutes = minutes - 60 * hours
print(hours, "hours and", minutes, "minutes")
