"""
编程中lambda函数，通常是需要一个函数，但是又不想费神
去命名一个函数，也就是匿名函数。
"""


# 将一个list里边的所有元素都平方
a = map(lambda x: x*x, [y for y in range(10)])
b = map(lambda x: x+1, [1, 2, 3])  # [2, 3, 4]
print(list(a))
print(list(b))
# map函数是将一个函数映射到一个枚举类型上面的。


# reduce函数是对一个序列的每一项进行迭代调用的函数，下面实例是求3的阶乘
from functools import reduce
c = reduce(lambda x, y: x*y, range(1, 4))
print(c)


