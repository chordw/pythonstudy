r = None
try:
    r = open('F:\python\python-study\.gitignore', 'r')
    print(r.read())
except IOError as e:
    print('找不到文件', e.filename)
finally:
    if r:
        r.close()
print("程序结束")
