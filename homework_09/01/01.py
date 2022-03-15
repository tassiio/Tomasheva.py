number = int(input("Enter any integer number:\n"))
odd_numbers = []
for i in range(number // 2):
    odd_numbers.append(2 * i + 1)
print("The list is", odd_numbers)

# upper = int(input('Введите число: '))
# print('Список из нечётных чисел от одного до N:',
# [odd_n for odd_n in range(1, upper+1, 2)])

# if name == '__main__':
# upper = int(input('Введите число: '))
# print('Список из нечётных чисел от одного до N:',
# [odd_n for odd_n in range(1, upper+1) if odd_n % 2 != 0])
