"""
python中，一个变量的作用域总是由代码中被赋值的地方所决定的
当python遇到一个变量的话，他会按照如下一个顺序进行搜索：
本地作用域（local），当前作用域被嵌入的本地作用域（encoding locals)
全局/模块（global），内置作用域（built-in)
"""