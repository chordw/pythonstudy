# 类和实例
# 类是抽象的模板
# 实例是根据类创建的具体的对象
# class关键字声明类

class Student(object):
    pass


act = Student()
aca = Student()
print(act)
print(aca)


# __init__(self,...)
# 有了__init__()方法，创建实例时就不能传入空的参数了，但self不用传
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。

class Teacher(object):
    def __init__(self, name, sex):
        self.__name = name
        self.__sex = sex

    def __str__(self):
        return 'name = %s,sex = %s' % (self.__name, self.__sex)

    pass


tcp = Teacher('张三', 'male')
tca = Teacher('张三', 'male')
print(tcp)
tcp.age = 90
print(tcp.age)
# print(tca.age)