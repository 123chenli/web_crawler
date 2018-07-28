"""
range和xrange都是在循环时使用
在执行range时，会在内存中创建一个列表。
xrange是一个懒惰评估的序列对象。在python2中存在，python3中不存在。
"""

for i in range(0, 100):
    print(i)

# for i in xrange(0, 100):
#     print(i)