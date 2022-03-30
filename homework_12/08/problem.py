import random


def integer(lst, length):
    for _ in range(length):
        lst[_] = int(lst[_])
    return list


max_number = int(input("Enter the max number:\n"))
Artem_number = random.randint(1, max_number)
# print(Artem_number)
if_yes = 0
numbers = []
while True:
    new_numbers = input("Is there Artem's number among these? ")

    if new_numbers != "Help!":
        new_numbers = new_numbers.split(' ')
        integer(new_numbers, len(new_numbers))
        if len(new_numbers) == 1 and new_numbers[0] == Artem_number:
            print("Artem number is", new_numbers[0])
            break

    else:
        print("Possible numbers of Artem:", numbers)
        break
    # print(new_numbers)

    for i in range(len(new_numbers)):
        if new_numbers[i] == Artem_number:
            print("Yes.")
            if_yes = 1
            for item in new_numbers:
                if item not in numbers:
                    numbers.append(item)
            if len(new_numbers) <= len(numbers):
                for item in numbers:
                    if item not in new_numbers:
                        numbers.pop(numbers.index(item))

    if if_yes == 0:
        print("No.")
        for item in new_numbers:
            if item in numbers:
                numbers.pop(numbers.index(item))

    # print("Numbers: ", numbers)

    if len(numbers) == 1:
        print("Artem's number is:", numbers[0])
        break
    if_yes = 0
