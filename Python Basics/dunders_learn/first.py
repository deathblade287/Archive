# x = [1, 2, 3]
# y = [4, 5, 6]

# print(x)
# print(len(x))

# print(len(y))
# print(y)

# z = x * y
# print(z)
# print(len(z))
# print(type(z))

import inspect
from queue import Queue as q

"""class Queue(q):
    def __repr__(self):
        return f"Queue({self._q_size()})"


qu = Queue()
print(qu)"""

v = inspect.getsource(q)


print(inspect.getdoc(q))
