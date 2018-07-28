# 输出结果为 1，没有改变原始值
# a = 1
# def fun(a):
#     a = 2
#
# fun(a)
# print(a)


# 地址发生变化
a = []
def fun(a):
    a.append(1)

fun(a)
print(a)