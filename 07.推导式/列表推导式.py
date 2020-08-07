"""
# for实现
list1 = []
for i in range(10):
     list1.append(i)
print(list1)
"""

"""
# for循环加if 创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)
"""

"""
list2 = []
for i in range(1, 3):
    for j in range(3):
        # 列表里面追加元组： 循环前准备一个空列表，然后这里追加元组数据到列表
        list2.append((i, j))
print(list2)
"""

# 列表推导式实现
list_1 = [i for i in range(10)]
print(list_1)

list1 = [i for i in range(0, 10, 2)]
print(list1)

list3 = [i for i in range(10) if i % 2 == 0]
print(list3)


list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

