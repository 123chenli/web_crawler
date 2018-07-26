# 实例变量,实例化后，每个实例单独拥有变量
class Test(object):
    num_of_instance = 0
    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == '__main__':
    print(Test.num_of_instance)  # 0
    t1 = Test('jack')
    print(Test.num_of_instance)  # 1
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)  # jack 1
    print(t2.name, t2.num_of_instance)  # lucy 2


class Person:
    name = []

p1 = Person()
p2 = Person()
p1.name.append(1)
print(p1.name)
print(p2.name)
print(Person.name)