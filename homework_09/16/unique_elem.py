# from itertools import groupby
first_list = []
print("Enter the first list of numbers (3):")
for _ in range(3):
    first_list.append(input())
second_list = []
print("Enter the second list of numbers (7):")
for _ in range(7):
    second_list.append(input())

print("The first list:", list(map(int, first_list)))
print("The second list:", list(map(int, second_list)))

first_list.extend(second_list)
first_list = list(map(int, first_list))
print("Combined list:", first_list)
print("Cleared list:", list(set(first_list)))

# coolest for the future
'''
first_list = [element for element, _ in groupby(sorted(first_list))]
print(first_list)
'''
