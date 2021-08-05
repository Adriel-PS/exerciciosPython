"""
collection deque


"""

from _collections import deque

deq = deque("adriel")

print(deq)
print(type(deq))

deq.append('y')
print(deq)
deq.appendleft("a")
print(deq)
print(deq.pop())
print(deq.popleft())
print(deq)
print(deq.pop)