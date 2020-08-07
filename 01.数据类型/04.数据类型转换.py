# 1. float() -- 将数据转换成浮点型
num1 = 1
str1 = '10'
list1 = [10, 20, 30]
s1 = {100, 300, 200, 500}
t1 = (100, 200, 300)

print(type(float(num1)))  # <class 'float'>
print(float(str1))  # 10.0

# 2. str() -- 将数据转换成字符串型
print(type(str(num1)))  # <class 'str'>

# 列表<====>元组<=====>集合<===>列表  三者可以互相转换

# 3. tuple() -- 将一个列表/集合转换成元组
print(tuple(list1))  # (10, 20, 30)
print(tuple(s1))  # (200, 100, 500, 300)

# 4. list() -- 将一个元组/集合转换成列表
print(list(t1))  # [100, 200, 300]
print(list(s1))  # [200, 100, 500, 300]

# 5. set() -- 将一个元组/列表转换成集合
print(set(list1))  # {10, 20, 30}
print(set(t1))  # {200, 100, 300}
