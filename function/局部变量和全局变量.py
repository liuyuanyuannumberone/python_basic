"""
局部作用域
"""


def test():
    n = 100
    print(n)  # 函数体内部访问，能访问到a变量


test()

m = 100


def test1():
    print(m)  # 全局变量


a = 100


def test2():
    a = 200  # 得到结论：这个a是局部变量
    print(a)  # 200


test2()
print(a)  # 100


def test3():
    global a  # 声明a为全局变量
    a = 200


test3()
print(a)

"""
总结：
    1. 如果在函数里面直接把变量a=200赋值，此时的a不是全局变量的修改，而是相当于在函数内部声明了一个新的局部变量
    2. 函数体内部修改全局变量： 先global声明a为全局变量，然后再变量重新赋值
"""
