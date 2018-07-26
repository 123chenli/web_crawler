"""
函数：第一个参数不是self的函数，不再类中定义的函数
方法：第一个参数是self的函数
实例：类的对象，instance
对象模型：就是实现对象行为的整个框架，分为经典和新的两种
"""


# 新式类,在创建的时候继承内置object对象，如list，dict
# class C(object):
#     pass
#
#
# # 经典类，直接声明
# class B:
#     pass


"""
新式类是广度优先，
旧式类是深度有限
下面是一个例子
"""


class A():
    def foo1(self):
        print('A')


class B(A):
    def foo2(self):
        pass


class C(A):
    def foo1(self):
        print('C')


class D(B, C):
    pass


d = D()
d.foo1()


"""
按照经典类的查找顺序从左到右深度优先的规则，
在访问d.foo1()的时候,D这个类是没有的..
那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),
所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过
"""