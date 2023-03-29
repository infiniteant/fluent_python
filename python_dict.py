# 散列表是字典类型性能出众的根本原因
from collections import abc

# 用来判断数据的映射类型
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))

try:
    tt = (1, 2, [30, 40])
    print(hash(tt))
except TypeError as e:
    print(f'the error is {e}')

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# 字典的构造方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)


# 字典推导
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
my_dict = {code: country.upper() for country, code in country_code.items() if code < 66}
print(my_dict)


# dict的update方法处理m的方式，是典型的'鸭子方法'

# 使用setdefault处理找不到的键
# import sys
# import re

# WORD_RE = re.compile('\w+')

# index = {}

# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
# for word in sorted(index, key=str.upper):
#     print(word, index[word])


# import sys
# import re

# WORD_RE = re.compile('\w+')

# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             index.setdefault(word, []).append(location)
# for word in sorted(index, key=str.upper):
#     print(word, index[word])


# my_dict.setdefault(key, []).append(new_value)

# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(new_value)


# 映射的弹性键查询
# 1.defaultdict：处理找不到的键的一个选择
from collections import defaultdict

dd = defaultdict(list)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
for k, v in s:
    dd[k].append(v)
for i in dd:
    print(i, dd[i])
print(dd['green'])

dd = defaultdict(int)
for k, v in s:
    dd[k] += 1
for i in dd:
    print(i, dd[i])
print(dd['green'])

# 特殊方法__missing__
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
try:
    print(d[1])
except KeyError as e:
    print(e)

print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))


# 字典的变种
from collections import OrderedDict

from collections import ChainMap

from collections import Counter

from collections import UserDict

# 子类化UserDict
import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item    


# 不可变的映射类型
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = 'x'
except TypeError as e:
    print(e)
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])