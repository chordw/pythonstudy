# <editor-fold desc="类和实例">


# 类和实例
# 类是抽象的模板
# 实例是根据类创建的具体的对象

# class关键字声明类
# (object) 表示要定义的类继承自object，object是所有类最终继承的类

class Student(object):
    pass


act = Student()
aca = Student()
print(act)
print(aca)


# __init__(self,...)
# 特殊方法“__init__”前后分别有两个下划线！！！
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

# </editor-fold>

# <editor-fold desc="访问限制">

# 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
# 就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Limited(object):
    def __init__(self, time, title):
        self.__time = time
        self.__title = title
        pass


lit = Limited(123, "访问限制")
# 无法直接通过对象直接访问私有属性
# 下面会报异常AttributeError：xx has no attribute '__time'
# print(lit.__time)
# 实际上Python解释器将私有变量改为名字_类名+变量名，如：_Limited__time
# 下面是可以访问的
print(lit._Limited__time)
lit._Limited__time = 90
print(lit._Limited__time)


# </editor-fold>

# <editor-fold desc="继承和多态">

# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）
class Animal(object):
    def eat(self):
        print("我会吃\n")

        pass


class People(Animal):
    pass


# 自定继承父类的方法和属性，还可以扩展方法和属性
People().eat()


# fell-like object 动态语言的鸭子类型

class Rock(object):

    def eat(self):
        print("我不会吃\n")
        pass


def eat(animal):
    animal.eat()


# Rock不是Animal的子类，仍然可以调用eat方法，只要对象具有eat方法即可
eat(Rock())

# </editor-fold>

# <editor-fold desc="获取对象信息">

# type()函数可以获取对象的Class类型
print(type(123))  # <class 'int'>
print(type(Rock()))  # <class '__main__.Rock'>

from types import FunctionType

print(type(eat))  # <class 'function'>
# 如何判断变量是一个函数？
print(type(eat) == FunctionType)

# isinstance() 判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
print(isinstance(People(), People))
print(isinstance(People(), Animal))
print(isinstance(Rock(), Animal))

# dir() 可以获取对象的所有属性和方法(包括继承的)，返回一个list
print(dir(Limited(123, 456)))

# hasattr() 判断对象是否有某个方法或属性
print(hasattr(lit, "time"))  # 没有该属性，编译器修改为_Limited__time
print(hasattr(lit, "_Limited__time"))
print(hasattr(Rock(), "eat"))

# getattr() 获取对象的某个属性或方法
print(getattr(Rock(), "eat"))
print(type(getattr(Rock(), "eat")) == FunctionType)

# setattr() 给对象设置一个属性
print(setattr(Rock(), "x", 123))

# </editor-fold>

# <editor-fold desc="实例属性和类属性">

# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
class ClassFile():
    name = "类属性"
    pass

print(ClassFile.name)

# </editor-fold>
