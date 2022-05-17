from lifo_cl import *
# length = int(input('Enter the length of the stack: '))
# stack = LIFO(length)

# print('Enter integer elements of the stack: ')
# for i in range(length):
#    stack.initial_push(int(input()))
# stack.pop()
# stack.push(int(input('Enter a new element: ')))
manager = TaskManager()
manager.new_task('housework', 3)
manager.new_task('homework', 3)
manager.new_task('urmaty', 1)
manager.new_task('python', 2)
print(manager)
