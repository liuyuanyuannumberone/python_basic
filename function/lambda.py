"""
如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
"""

# def fn1():
#     return 100

# def add(a, b):
#     return a + b

# lambda  匿名函数  lambda 参数列表: 表达式
fn2 = lambda: 100
# print(fn2)  # lambda内存地址
# print(fn2())  # 10

fn4 = lambda a: a
# print(fn4('hello world'))  # hello world


# lambda
fn3 = lambda a, b: a + b
# print(fn3(2, 3))


# 默认参数
fn5 = lambda a, b, c=100: a + b + c
# print(fn5(10, 20))  # 130
# print(fn5(10, 20, 200))  # 230

# 可变参数：*args 返回一个元组
fn6 = lambda *args: args
print(fn6(10, 20)) # (10, 20)
print(fn6(10, 20, 30, 40))
print(fn6(10))


# 可变参数：**kwargs 返回一个字典
fn7 = lambda **kwargs: kwargs
print(fn7(name='Python'))
print(fn7(name='Python', age=30))   # {'name': 'Python', 'age': 30}


# lambda 两个数字比大小，谁大返回谁
fn8 = lambda a, b: a if a > b else b
print(fn8(1000, 500))