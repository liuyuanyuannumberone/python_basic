
"""
多行注释
"""


'''
多行注释
'''

num1 = 1  # int整型
print(type(num1))  # <class 'int'>

num2 = 1.1  # float 浮点型
print(type(num2) == "<class 'float'>")  # False      # <class 'float'>
print(type(num2) == 'float')  # False

b = True | False  # bool 布尔
print(type(b))  # <class 'bool'>

a = 'hello world'  # str 字符串
print(type(a))  # <class 'str'>

c = [10, 20, 30]  # list 列表
print(type(c))  # <class 'list'>

d = (10, 20, 30)  # tuple -- 元组
print(type(d))  # <class 'tuple'>

e = {10, 20, 30}  # set -- 集合
print(type(e))  # <class 'set'>

f = {'name': 'TOM', 'age': 18}  # dict -- 字典 -- 键值对
print(type(f))  # <class 'dict'>

