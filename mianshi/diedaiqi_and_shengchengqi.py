"""
面试题：将列表生成式中[]改为（）之后，数据结构是否发生变化？
答：是，从列表变成生成器


"""
L = [x*x for x in range(10)]
print(L)
G = (x*x for x in range(10))
print(G)