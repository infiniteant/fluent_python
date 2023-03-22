'''双向队列和其他形式的队列'''
from collections import deque

# maxlen是可选参数,代表这个队列可以容纳的元素的数量，而且一旦设定，这个属性就不能修改了
dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)


dq.extendleft([10, 20, 30, 40])
print(dq)