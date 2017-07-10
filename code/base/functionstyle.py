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

