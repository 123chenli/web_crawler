"""
单例模式是一种常用的软件设计模式。它的核心结构中只包含一个被称为
单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该
实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望
在系统中某个类的对象只能存在一个，单例模式是最好的解决方案

__new__（）在__init__()之前被调用，用于生成实例对象。利用这个方法
和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，
单例模式设计的类只能实例
重点，常考
"""


# 1、使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


# 2、共享属性
"""
创建实例时把所有实例的__dict__指向同一个字典，
这样他们具有相同的属性和方法
"""


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


# 3、装饰器版本
def singleton(cls):
    instance = {}
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance


@singleton
class MyClass:
    a = 1


# 4、作为python的模块是天然的单例模式
class My_Singleton(object):

    def foo(self):
        pass


my_singleton = My_Singleton()

from mysingleton import my_singleton

my_singleton.foo()


