name_list = ['TOM', 'Lily', 'ROSE']
print(name_list)
print(len(name_list))
print(name_list[1])


# index(字串，开始位置的下标，结束位置的下标)
print(name_list.index('TOM'))  # 0
# print(name_list.index('TOMS'))

#  count()
print(name_list.count('TOM'))  # 1
print(name_list.count('TOMS'))  # 0

#  in 判断是否存在
print('TOM' in name_list)  # True
print('TOMS' in name_list)  # False
print('TOMs' not in name_list)  # True


name = input('请输入您的邮箱账号名:')

if name in name_list:
    print(f'您输入的名字是{name}, 此用户名已经存在')
else:
    print(f'您输入的名字是{name}, 可以注册')
