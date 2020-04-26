t1 = ('aa', 'bb', 'cc', 'bb')

# 1. 下标
print(t1[0])  # aa


# 2. index()
print(t1.index('bb')) # 1
# print(t1.index('bbb'))  # ValueError: tuple.index(x): x not in tuple

# 3. count()
print(t1.count('aa'))  # 1
print(t1.count('aaa'))  # 0

# 4. len()
print(len(t1))  # 4


t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[2])  # ['cc', 'dd']
print(t2[2][0]) # cc
t2[2][0] = 'TOM'  # 可以
# t2[2]=[];  # error TypeError: 'tuple' object does not support item assignment
'''
元组内的数据不允许修改
'''
print(t2)  # ('aa', 'bb', ['TOM', 'dd'])




