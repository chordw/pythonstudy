# 异常处理体系：try...except...finally...
# 记录错误：logging

import logging

# 捕获错误，打印日志
try:
    n = int("1")
except ValueError as e:
    logging.error(e)
    print("数值转换错误")
finally:
    print("退出了程序")



# 抛出错误：raise关键字可以抛出一个错误对象

def foo():
    raise BaseException("自定义错误")


# 调试
# 断言：assert，后面的表达式应该是True，如果断言失败，则assert会抛出AssertionError错误