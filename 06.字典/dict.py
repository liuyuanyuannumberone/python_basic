"""
创建字典
"""
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
dict2 = {}
dict3 = dict()

print(type(dict1))
print(type(dict2))
print(type(dict3))

dict1['id'] = 110
print(dict1)
dict1['name'] = 'lyy'
print(dict1)

"""
del 删除字典或指定的键值对
# del(dict1)  # 报错
"""

# del dict1['name']  #删除键值对
# print(dict1)

# dict1.clear()  # 清除所有
# print(dict1)  # {}
"""
查找
"""
print("=======================")
# print(dict1)  # {'name': 'lyy', 'age': 20, 'gender': '男', 'id': 110}


print(dict1['name'])  # 返回对应的值(key存在)
print(dict1.get('name'))
print(dict1.get('names'))  # 如果key不存在，返回None

# keys() 查找字典中所有的key，返回可迭代对象
print(dict1.keys())  # dict_keys(['name', 'age', 'gender', 'id'])
# values() 查找字典中的所有的value，返回可迭代对象
print(dict1.values())  # dict_values(['lyy', 20, '男', 110])
# items() 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组
print(dict1.items())  # dict_items([('name', 'lyy'), ('age', 20), ('gender', '男'), ('id', 110)])

print("======================================")
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for key, value in dict1.items():
    print(f'{key}={value}')



