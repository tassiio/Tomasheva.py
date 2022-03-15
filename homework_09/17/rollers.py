pairs = int(input("Enter the amount of pairs:\n"))
sizes = []
for i in range(pairs):
    sizes.append(input(f'The size of the pair № {i + 1} : '))

people = int(input('Enter the amount of people:\n'))
foot_sizes = []
for i in range(people):
    foot_sizes.append(input(f'Foot size of № {i + 1} : '))

sizes = list(map(int, sizes))
foot_sizes = sorted(list(map(int, foot_sizes)))

sizes = [sorted(sizes)[-people:] if pairs > people else sorted(sizes)[-pairs:]]
sizes = sizes[0]
print(sizes)
print(foot_sizes)

amount = 0
for i in range(len(sizes)):
    for k in range(len(foot_sizes)):
        if foot_sizes[k] <= sizes[i]:
            del foot_sizes[k]
            amount += 1
            break
print(amount)
