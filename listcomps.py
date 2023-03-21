# 不使用列表推导式
symbols = '$￥&*()^&%#'
beyond_ascii = [ord(s) for s in symbols]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)


# 笛卡儿积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


# 元组和记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, eara = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 元组拆包
# 可以使用*运算符把一个可迭代对象拆开作为函数的参数
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

import os
# _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
_, filename = os.path.split('C:/User/Downloads/test.txt')
print(filename)

# 使用*处理剩下元素
a, b, *test = range(5)
print(a, b, test)

a, *test, b = range(4)
print(test)

# 嵌套元素拆包
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# 具名元组
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

# 具名元组的专有属性
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ":" , value)

# 作为不可变列表的元组
