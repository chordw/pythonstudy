# <editor-fold desc="list">
# 集合list的使用，list是一个可变的有序表

# list的定义与赋值
classmates = ['a', 'b', 'c']
print(classmates)

# 集合的长度len()方法传入集合对象
print(len(classmates))

# 访问集合中的元素,下标从0开始到长度-1   如果越界会报出IndexError: list index out of range错误
print(classmates[0])
# 注意正序是从0开始，倒序是从-1开始
print(classmates[-1])
# 在list末尾追加元素
print('追加前的集合：')
print(classmates)
classmates.append('d')
print('追加后的集合：')
print(classmates)

# 在list某个位置插入一个元素，，依次后移
print('插入前后的集合：')
print(classmates)
print('插入后的集合：')
classmates.insert(1, 'e')
print(classmates)

# 删除末尾的元素

print('删除前的集合：')
print(classmates)
print('删除后的集合：')
classmates.pop()
print(classmates)

# 删除指定位置的元素
print('删除第二个元素前的集合：')
print(classmates)
print('删除第二个元素后的集合：')
classmates.pop(1)
print(classmates)

# 替换list中的某个元素
print('替换前的集合：')
print(classmates)
print('替换后的集合：')
classmates[1] = 123
print(classmates)

# list中可以存储不同类型的数据：字符串类型，数值类型，boolean类型，list类型

# </editor-fold>

# <editor-fold desc="tuple">
# 元组tuple的使用，，有序的集合,,一旦初始化后，数据不能再修改,,只是指向不变，
# 比如说元组中有一个list，list内是可以变化的

# 元组的定义
meta = ('A', 'B', ['a', 'b'])
# 元组的访问和list一样，只是没有了append(),insert(),pop(),这样的方法
print("元组meta的长度：", (len(meta)))
print(meta)

# </editor-fold>
