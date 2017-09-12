# python 的高阶特性

# 切片操作符 Slice
# 取list或者tuple中n-m位置的元素  n<=m
a = list(range(10))  # 生成1-10的数列

# 取的是从list的从n到m索引位置的元素，包括n位置，但不包括m位置
print(a[0:11])

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

# 列表生成式 list comprehensions 用来创建list
f = [x * x for x in range(1, 11)]
print('列表生成器：', f)
print('列表生成器Ⅱ：', [m + n for m in 'abc' for n in 'edf'])

import os

# 当前目录下所有文件和文件夹的名字
print([d for d in os.listdir('.')])
print(os.listdir("."))

g = ['JDAFa', 123, 'kkkEEEAD']
print([isinstance(s, str) for s in g])

# 生成器
# 一边循环一边计算的机制，称为生成器：generator
# 创建生成器
# 第一种方法： 将列表生成式的方括号改为小括号
h = (m + n for m in 'q' for n in 'asd')
# for hh in h:
#     print(hh)
# 创建list和generator区别就在于最外层的()和[]
# generator保存的是算法，调用next(生成器名字)方法可以计算出g的下一个元素，没有更多的元素是会爆出StopIteration的错误
print('生成器h的第一个值：', next(h))
print('生成器h的第二个值：', next(h))
print('生成器h的第三个值：', next(h))


# 斐波拉契数列
def fab(m):
    n, a, b = 0, 0, 1;
    while n < m:
        print(b)
        a, b = b, a + b
        n = n + 1
    return '结束'


print(fab(19))


# 第二种方法创建生成器
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 例如上边的函数斐波拉契数列
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b;
        a, b = b, a + b
        n = n + 1
    return "结束了"


fib = fib(9)
for m in fib:
    print("斐波拉契：", m)

print([1] + [2])
print(range(0))


# 输出杨辉三角
def triangles(n):
    L = [1]
    m = 1
    while m <= n:
        yield L
        L = [1] + [L[x] + L[x + 1] for x in range(len(L) - 1)] + [1]
        m = m + 1
    return "结束了"


tri = triangles(10)
for tr in tri:
    print(tr)

# 迭代器
# 可迭代对象Iterable:一类是集合数据类型：list，tuple，dict，set,str ：一类是：generator类型：生成器和包含yield字段的function

# 判断一个对象是不是可迭代对象 isinstance()
from collections import Iterable
from collections import Iterator

print(isinstance(range(0, 8), Iterable))

# 生成器不但可以作用于for循环，，还可以被next()函数不断调用返回下一个值，知道抛出StopIteration
# 可以被next()函数调用并不断返回值的对象，被称为迭代器：Iterator
# 生成器都是迭代器  但是list dict tuple set str 虽然是Iterable 但不是Iterator
print('list是迭代器吗：', isinstance(range(1), Iterator))
print('str是迭代器吗：', isinstance('1', Iterator))
print('tuple是迭代器吗：', isinstance((1, 2), Iterator))
print('dict是迭代器吗：', isinstance({'a': 1, 'b': 2}, Iterator))
# 但可以把上述类型转为迭代器iter()
print('iter(list)是迭代器吗：', isinstance(iter(range(1)), Iterator))
