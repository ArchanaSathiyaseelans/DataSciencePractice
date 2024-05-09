import numpy as np
import time
import sys

# so numpy is faster
l = range(1000)
print(sys.getsizeof(5) *len(l))

array = np.arange(1000)
print(array.size*array.itemsize)