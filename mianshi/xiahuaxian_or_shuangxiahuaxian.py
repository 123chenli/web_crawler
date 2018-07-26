"""
1、__foo__: 一种约定，python内部的名字，用来区别其他用户自定义的命名，以防冲突，
例如：__init__(),__del__(),__call__()
2、_foo: 一种约定，用来指定变量私有的一种方式，不能用from module import * 来导入，
其它方面和共有一样访问
3、__foo: 解析器用_classname__foo来代替这个名字，以区别和其他类相同的命名，它无法
直接像共有成员一样随便访问，可以通过对象名._类名__xxx的方式来访问
"""
class Myclass(object):
    def __init__(self):
        self.__superprivate = 'hello'
        self._semiprivate = 'world'

mc = Myclass()
# print(mc.__superprivate),显示Myclass没有此属性
print(mc._semiprivate)
print(mc.__dict__)