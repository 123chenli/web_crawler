"""
装饰器是怎样工作的
"""

def makebold(fn):
    def wrapped():
        return '<b>' + fn() + '<b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped


@makebold
@makeitalic
def hello():
    return 'hello world'

print(hello())