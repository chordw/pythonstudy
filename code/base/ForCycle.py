#For循环,格式for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
names = ['张三','李斯','黎明']
for name in names :
	if name == '张三':
		print(name)
		
#求和
sum = 0;
for x in [1,2,3,4,5,6,7,8,9]:
	sum =sum + x;
print(sum)

#生成整数数列 range()
print(range(100))
sum = 0;
for x in range(101):
	sum =sum + x;
print(sum)

#while循环 
''' 多行注释
	只要条件满足，就不断循环；条件不满足时退出循环。
'''



sum = 0
n = 99
while n>0:
	sum = sum + n
	n = n-2;
print(sum)