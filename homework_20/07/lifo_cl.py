class LIFO:
    def __init__(self, length=1):
        assert length > 0, "Length should be positive"
        self.length = length
        self.current_item = 0
        self.array = [0] * self.length

    def initial_push(self, item):
        assert self.current_item < self.length
        self.array[self.current_item] = item
        self.current_item += 1

    def pop(self):
        assert self.current_item != 0
        print('Top item of the stack: ', self.array[self.length - 1], 'DONE', '\n')
        del self.array[self.length - 1]
        self.length -= 1
        # print('Now your stack is (after extracting the last element): ', self.array)

    def push(self, new_element):
        new_array = [0] * self.length
        for i in range(self.length):
            new_array[i] = self.array[i]
        new_array.append(new_element)
        self.length += 1
        self.array.clear()
        self.array = new_array
        # print('Now your stack is (after adding a new element:', self.array)

    def get_lifo(self):
        return str(list(reversed(self.array)))


class TaskManager:
    def __init__(self):
        self.dictionary = dict()

    def new_task(self, task: str, priority: int):
        if priority not in self.dictionary.keys():
            self.dictionary[priority] = list()
            self.dictionary[priority].append(task)
        else:
            self.dictionary[priority].append(task)
        self.dictionary = dict(sorted(self.dictionary.items(), key=lambda x: x[0]))

    def __str__(self):
        self.lifo = LIFO(len(self.dictionary))
        items = list(self.dictionary.items())
        y = {k: v for k, v in reversed(items)}
        for key in y.keys():
            self.lifo.initial_push(str(key) + ': ' + str(y[key]))
        print('Priorities: ')
        print(self.lifo.get_lifo())
        self.lifo.pop()

        return self.lifo.get_lifo()
