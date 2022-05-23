from sqrt_cl import Sqrt


def sqrt_func(numb: int):
    counter = 0
    if numb < 0:
        print('Enter a positive number.')
    else:
        while counter < number:
            counter += 1
            yield counter ** 2


number = int(input('Print any integer number: '))

print('From class: ')
sqrts = Sqrt(number)
for element in sqrts:
    print(element, end=' ')

print('\nFrom function-generator:')
sqrts_functional = sqrt_func(number)
print(next(sqrts_functional), end=' ')
print(next(sqrts_functional), end=' ')
print(next(sqrts_functional), end=' ')
print(next(sqrts_functional), end=' ')
print(next(sqrts_functional), end=' ')

print('\nFrom generator expression:')
print(*[i ** 2 for i in range(1, number + 1)], end=' ')
