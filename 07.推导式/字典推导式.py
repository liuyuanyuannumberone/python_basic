# 创建字典 key是1-5的数字，v是这个数字的平方
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)


list1 = ['name', 'age', 'gender', 'id']
list2 = ['Tom', 20, 'man']

dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)


counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 1. 需求：提取电脑台数大于等于200
# 获取所有键值对数据，判断v值大于等于200 返回  字典
print(counts.items())
dict3 = {key: value for key, value in counts.items() if value >= 200}
print(dict3)
