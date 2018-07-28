"""
自省是面向对象语言编写的程序在运行时，知道对象的类型
有type(),getattr(),hasattr(),isinstance()
"""

a = [1, 2, 3]
b = {'a': 1, 'b': 2, 'c': 3}
c = True
print(type(a),type(b), type(c))
print(isinstance(a, list))