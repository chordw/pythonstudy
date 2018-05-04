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
with open('F:\python\python-study\README.md', 'r', encoding='utf-8') as f:
    print(f.read())

# for循环读取到内存中，避免占用内存过大
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

