"""
super()函数是用调用父类（超类）的一个方法
是用来解决多重继承的问题，直接用类名调用父类
方法在使用单继承的时候没问题，但是如果使用多继承
，会涉及到查找顺序（MRO),重复调用（钻石继承）等
多种问题。（MRO就是类的方法解析顺序表，也是继承
父类方法时的顺序表）
语法：super(type[,object-or-type])
type:类
object-or-type:类，一般是self
"""


# python3中super的实例
# class A:
#     pass
# class B(A):
#     def add(self, x):
#         super().add(x)


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self)
        #  首先找到 FooChild 的父类（就是类 FooParent），
        # 然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    print('aaa')
    fooChild.bar('HelloWorld')
