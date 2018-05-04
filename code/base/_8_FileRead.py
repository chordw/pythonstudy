# 读写文件是最常见的IO操作
r = None
try:
    # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，操作系统同一时间能打开的文件数量是有限的。
    r = open('F:\python\python-study\README.md', 'r', encoding='utf-8')
    print(r.read())
except IOError as e:
    print('找不到文件', e.filename)
finally:
    # 判断null
    if r:
        r.close()
print("程序结束")

# 自带关闭文件对象的方法
# Python引入了with语句来自动帮我们调用close()方法
with open('F:\python\python-study\README.md', 'r', encoding='utf-8') as f:
    print(f.read())

# for循环读取到内存中，避免占用内存过大
# read(size)，每次读取size个字节的内容
# readline()，每次读取一行内容
# readlines()，读取多有行，返回一个list
# 二进制文件要以“rb”模式open文件
# 非utf-8文本文件要传入encoding参数：open("/../..","rb",encodeing="gbk")
try:
    f = open('F:\python\python-study\README.md', 'r', encoding='utf-8')
    for line in f.readline():
        print(line.strip())
except IOError as e:
    e.with_traceback()
finally:
    if f:
        f.close()

from io import StringIO

f = StringIO()
f.write("你好吗")
print(f.getvalue())

import os
print(os.environ)

# 写文件
# 写文件和读文件唯一区别：open("/..//","w",encoding="gbk")，参数传 w或者wb
# f.close()调用时数据才会被些人磁盘
# 写文件使用with语句比较保险
# w模式写文件时，如果文件已经存在则覆盖内容，想要追加文件末尾内容，可以传入a，以追加模式写入
with open('F:\python\python-study\README.md', 'a',encoding='UTF-8') as f:
    f.write("你好")
