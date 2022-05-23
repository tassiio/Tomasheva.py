class Sqrt:
    def __iter__(self):
        self.counter = 0
        return self

    def __init__(self, limit: int):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration
