# 函数式编程
# 高阶函数 higher-order function
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 函数本身可以赋给变量即：变量可以指向函数
ff = abs
print(ff(-2))


def add(x, y, f):
    return f(x) + f(y)


print(add(3, -7, ff))

# map()函数:返回的是一个迭代器
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
print(map(abs, [1, -1, -2, 0, -111]))
# map返回的Iterator是惰性序列
print(list(map(abs, [1, -1, -2, 0, -111])))
print(list(map(str, range(100))))

# reduce()函数：
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

arr = [1, -2, 3, -4, 6]


def add(x, y):
    return x + y


print(reduce(add, arr))

# filter()函数：用于过滤数列,,筛选函数
'''
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''


# 删除序列中的奇数
def id_odd(n):
    return n % 2 == 1


print(list(filter(id_odd, arr)))

'''
sorted()函数：用于排序算法
'''
# 按绝对值从小到大排序
print(sorted([36, 5, -12, 9, -21], key=ff))
# 忽略大小写排序
print(sorted(['adf', 'dcA', 'Cae'], key=str.lower))
# 反序
print(sorted(['adf', 'dcA', 'Cae'], key=str.lower, reverse=True))

from operator import itemgetter

# 用sorted()排序的关键在于实现一个映射函数。
student = [('kk', 2), ('hh', 8), ('Cc', 7), ('aA', 1)]
print(sorted(student, key=itemgetter(1)))


# 闭包
def return_def(*s):
    def sum():
        su = 0
        for x in s:
            su = su + x
        return su

    return sum


fff = return_def(1, 23, 56, 89)
print(fff())


# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 匿名函数
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
# 匿名函数lambda x: x * x  ：关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数可以直接赋给变量，然后通过变量调用函数
# 匿名函数只能有一个表达式，所以不用写return
gg = lambda x: x * x
print(gg(9))


# 装饰器
# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 比如：在函数调用前后自动打印日志
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('调用了 %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def sum(x, y):
    return x + y


print(sum(19, 21))
