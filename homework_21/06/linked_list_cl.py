class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next_el = None

    def __init__(self, *args):
        length = len(args)
        self.__length = length
        self.__head = self.__Node(args[0]) if length > 0 else None
        self.__tail = self.__head
        for i in range(1, length):
            self.__tail.next_el = self.__Node(args[i])
            self.__tail = self.__tail.next_el

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.next_el

    def __str__(self):
        return f"[{' '.join(str(i) for i in self)}]"

    def __len__(self):
        return self.__length

    def __index_check(self, index):
        if not 0 <= index < self.__length:
            raise IndexError

    def append(self, value):
        if self.__length > 0:
            self.__tail.next_el = self.__Node(value)
            self.__tail = self.__tail.next_el
        else:
            self.__head = self.__tail = self.__Node(value)
        self.__length += 1

    def get(self, index):
        self.__index_check(index)
        current = self.__head
        for _ in range(index):
            current = current.next_el
        return current.value

    def remove(self, index):
        self.__index_check(index)
        if self.__length == 1:
            self.__head = self.__tail = None
        elif index == 0:
            self.__head = self.__head.nxt
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next_el
            current.next_el = current.next_el.next_el
            if index == self.__length - 1:
                self.__tail = current
        self.__length -= 1
