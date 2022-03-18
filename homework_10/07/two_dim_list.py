#
# import numpy
#
# two_dim = numpy.random.randint(1, 100+1, size=[4, 3])
# print(two_dim)

import random

two_dim = [[random.randint(1, 100) for _ in range(3)] for _ in range(4)]
print(two_dim)
