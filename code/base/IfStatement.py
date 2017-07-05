#Python中的if else if
def age():
	print('输入您的年龄：')
	age = input()
	age = int(age)
	if age >30:
		print('而立之年')
	elif age >40:
		print('中年')
	elif age >20:
		print('少年啊')
		
age()
