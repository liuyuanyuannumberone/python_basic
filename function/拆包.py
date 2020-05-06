# 拆包元组数据
def return_num():
    return 100, 200


result = return_num()
print(result)  # (100, 200)

num1, num2 = return_num()
print(num1)
print(num2)


# 字典数据拆包: 变量存储的数据是key值
dict1 = {'name': 'TOM', 'age': 20}
a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])

