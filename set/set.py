"""
集合有去重功能
"""
s1 = {10, 20, 30, 40, 50}
print(s1)  # <class 'set'>、

s3 = set('abcdefg')
print(s3)

s4 = set()
print(s4)  # set()

print("============")
s5 = {10, 20}
s5.add(100)
s5.add(100)  # 集合有去重功能，如果追加的数据是集合已有数据，则什么事情都不做
s5.add(1)  # {100, 1, 10, 20}
s5.add(2)  # {1, 2, 100, 10, 20}
s5.add(3)  # {1, 2, 3, 100, 10, 20}
# print(s5)


# update()：增加的数据是序列
s6 = {10, 20}
s6.update([10, 20, 30, 40, 50])
print(s6)  # {40, 10, 50, 20, 30}



# remove(): 删除指定数据，如果数据不存在报错
s6.remove(10)
print(s6)  # {40, 50, 20, 30}

# discard()：删除指定数据，如果数据不存在不报错
s6.discard(10)
print(s6)

# pop(): 随机删除第一个数据，并返回这个数据
del_num = s6.pop()
print(del_num)

print(10 in s6)  # False
print(10 not in s6)  # True




