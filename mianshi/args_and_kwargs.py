"""
当不确定函数里将要传递参数的个数时，使用*args
"""

def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}.{1}'.format(count, thing))


if __name__ == '__main__':
    print_everything('apple', 'banana', 'cabbage')


"""
相似的，**kwargs是没有事先定义的参数名
"""


def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0}={1}'.format(name, value))


if __name__ == '__main__':
    table_things(apple='fruit', cabbage='vegetable')

"""
也可以混用，命名参数首先获得参数值然后所有的其他参数都传递给*args和**kwargs
例如：def table_thing(titlesting, **kwargs)
但是必须注意，*args同时定义在函数中时，*args必须在**kwargs前面
当调用函数时，可以用*和**的语法，如下：
"""

def print_three_things(a, b, c):
    print('a={0}, b={1}, c={2}'.format(a, b, c))


if __name__ == '__main__':
    mylist = ['aaaak', 'bbbbk', 'cccck']
    print_three_things(*mylist)