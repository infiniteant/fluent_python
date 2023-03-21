# 为什么切片和区间会忽略最后一个元素
'''
优势:
    1.当只有最后一个位置信息时，我们可以快速看出切片和区间里有那几个元素
    2.当起止位置信息都可见时，我们可以快速计算出切片和区间的长度
    3.我们可以利用任意一个下标把序列分割成不重叠的两部分
'''
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])


# 对对象进行切片
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

invoice = '''
0.....6................................40........52...55........
1909  Pimoroni PiBrella                 $17.50    3    $52.50
1489  6mm Tactile Switch x20            $4.95     2    $9.90
1510  Panavise Jr. - PV-201             $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240            $34.95    1    $34.95
'''
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:] 
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


# 多维切片和省略


# 给切片赋值
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# 如果赋值的对象是一个切片
try:
    l[2:5] = 100
except Exception as e:
    print(e)
l[2:5] = [100]
print(l)

# 对序列使用+和*
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

# 建立有列表组成的列表
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))

l = [1, 2, 3]
print(id(l))
l += [2]
print(id(l))

t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except Exception as e:
# except Exception:
    # print(Exception)
    print(type(e))
    print(e)
print(t)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))

print(fruits)

print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))
print(fruits)
fruits.sort()
print(fruits)