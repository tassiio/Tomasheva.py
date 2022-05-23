class QHofstadter:
    def __iter__(self):
        return self

    def __init__(self, list_numb: list):
        self.list_numb = list_numb

    def __next__(self):
        try:
            q_n = self.list_numb[-self.list_numb[-1]] + self.list_numb[-self.list_numb[-2]]
            self.list_numb.append(q_n)
            return q_n
        except IndexError:
            raise StopIteration

    def get_sequence(self):
        return self.list_numb
