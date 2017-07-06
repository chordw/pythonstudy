#调用python内置的函数
print(abs(-111))#求绝对值
#调用函数的时候，如果参数数量不对，会报TypeError
#print(abs(1,2))
#print(abs('a'))#参数格式不对

print(max(122,45,-123,898))#参数中任意多个数值的最大值
print(min(121,2323,-234,-3435))#参数中任意多个数值的最小值

print(int('-124'))#类型转换，将字符串转为数值类型
#print(int('a'))#会报ValueError


#自定义函数
#def 函数名(0到多个参数逗号分隔参数)：
def my_abs(a):
	if a>=0:
		return a;
	else:
		return -a;
		
print(my_abs(-11))