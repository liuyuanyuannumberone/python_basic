name_list = ['TOM', 'Lily', 'ROSE']

#  del 删除列表
# del name_list
# print(name_list)  # name 'name_list' is not defined

# del 可以删除指定下标的数据
# del name_list[0]
# print(name_list)  # ['Lily', 'ROSE']

# pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
# del_name = name_list.pop()
# del_name = name_list.pop(1)
# print(del_name)
# print(name_list)

# remove(数据) 移除数据
# name_list.remove('ROSE')
# print(name_list)

#  clear() -- 清空
# name_list.clear()
# print(name_list)


# 修改指定下标的数据
# name_list[0] = 'aaa'
# print(name_list)


# 逆序 reverse()
list1 = [1, 3, 2, 5, 4, 6]
# list1.reverse()
# print(list1)

# sort() 排序：升序(默认) 和 降序
# list1.sort()   # [1, 2, 3, 4, 5, 6]
# list1.sort(reverse=False)  # [1, 2, 3, 4, 5, 6]
list1.sort(reverse=True)  # [6, 5, 4, 3, 2, 1]
print(list1)

list2 = list1.copy()
print(list2)
