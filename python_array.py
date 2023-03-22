from array import array
from random import random


floats = array('d', (random() for i in range(10**7)))

print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

# Python3.4之后数组不在支持就地排序的方法
a = array('d', (random() for i in range(3)))
a = array(a.typecode, sorted(a))
print(a)


# 内存视图
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))

print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)

import numpy
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2][1])
print(a[:,1])
print(a.transpose())

floats = numpy.loadtxt('output.txt')
print(floats[-3:])

floats *=.5
print(floats[-3:])

from time import perf_counter as pc

t0 = pc()
print(t0)
floats /= 3
print(pc()- t0)

numpy.save('output', floats)
floats2 = numpy.load('output.npy', 'r+')
floats2 *= 6
print(floats2[-3:])