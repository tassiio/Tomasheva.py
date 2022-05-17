velocity = float(input("Put Vasya's velocity: \n"))
hours = float(input("Put amount of hours: \n"))
path = velocity * hours
# print(path)
rounds = path // 115
# print(rounds)
print(path - rounds * 115)
