# python 的高阶特性

# 切片操作符 Slice
# 取list或者tuple中n-m位置的元素  n<=m
a = list(range(5))  # 生成1-10的数列

# 取的是从list的从n到m索引位置的元素，包括n位置，但不包括m位置
print(a[-11:11])

# 迭代 for···in的方式完成迭代
# for循环就是迭代

# 迭代list和tuple
for x in a:
    print(x)

b = tuple(range(3))
for x in b:
    print(x)

# 迭代dict dict默认迭代的是key
d = {"a": 1, "b": 2, "c": 3}
for b in d:
    print(b)

# 迭代dict的value
for v in d.values():
    print(v)

# 同时迭代dict的key 和value
for k, v in d.items():
    print(k, v)

# 字符串也可以迭代
for s in "你好吗":
    print(s)

# 对于任何可迭代的对象 for 都可以正常的执行
# 判断一个对象是否可以迭代：方法是通过collections模块的Iterable类型判断
from collections import Iterable

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(d, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对
e = enumerate(a)
for i, v in e:
    print(i, v)
