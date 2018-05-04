# 调用python内置的函数
print(abs(-111))  # 求绝对值
# 调用函数的时候，如果参数数量不对，会报TypeError例如TypeError: abs() takes exactly one argument (2 given)
# print(abs(1,2))
# print(abs('a'))#参数格式不对

print(max(122, 45, -123, 898))  # 参数中任意多个数值的最大值
print(min(121, 2323, -234, -3435))  # 参数中任意多个数值的最小值

print(int('-124'))  # 类型转换，将字符串转为数值类型


# print(int('a'))# 会报ValueError


# 自定义函数
# def 函数名(0到多个参数逗号分隔参数)：
def my_abs(a):
    if a >= 0:
        return a
    else:
        return -a


print(my_abs(-11))

# 递归函数
'''
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
'''


def fact(n):
    if n <= 0:
        return "输入的数值需要大于0"
    if n == 1:
        return 1
    return n * fact(n - 1)


print('请输入数字：')
m = int(input())
print(m, '的阶乘=', fact(m))
