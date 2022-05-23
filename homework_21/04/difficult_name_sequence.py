from difficult_name_sequence_cl import QHofstadter

sequence = QHofstadter([1, 0])
# print([next(sequence) for i in range(10)])


def qhofstadter(lst):
    while True:
        try:
            print(lst[-lst[-1]], lst[-lst[-2]])
            q_n = lst[-lst[-1]] + lst[-lst[-2]]
            lst.append(q_n)
            yield q_n
        except IndexError:
            return


print(next(qhofstadter([1, 2])))
