amount = int(input("How many elements are in your list?\n"))
initial_list = [int(input(f'{i + 1}: ')) for i in range(amount)]

print(initial_list)
new_list = [initial_list[i] for i in range(amount) if initial_list[i] != 0]
zeros = initial_list.count(0)
for _ in range(zeros):
    new_list.append(0)
print(new_list)

for i in range(len(new_list) - 1, len(new_list) - zeros - 1, -1):
    new_list.pop(i)
print(new_list)
