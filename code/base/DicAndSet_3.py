# dict 字典以键值对的形式存储数据，，一个key只能对应一个value，，重复放入后面的会把前面的覆盖掉

people = {'zz': 34, 'uu': 54}
print(people)

# 从dict中取值
print('zz对应的value是：', people['zz'])
# 如果没有对应的key,,会报KeyError的错误
# print(people['tt'])

# 判断dict中是否存在某个key，有两种方式  key in dictName  或者  根据dictName.get(key)的返回值，若没有会返回None
print('34' in people)
if ('uu' in people):
    print("dict:people中含有34这个key")
print(people.get("45"))
print(people.get('34', '没有这个元素'))  # 第二个参数是没有key该key时value的默认值

# set是一组key的集合，不存储value，由于dict的key不能重复，所以set里没有重复的元素
# set的创建::需要一个list作为输入集合
# 重复元素在set中自动被过滤掉
s = {1, 2, 2, 3}
s.add(3)
print(s)

# 可以通过add()方法向set中添加元素
s.add(4)
print(s)
# 可以通过remove()方法删除set中的元素,,如果没有这个元素，会报KeyError的错误
s.remove(4)
print(s)

# 遍历set
for ss in s:
    print(ss)

exit(999)
