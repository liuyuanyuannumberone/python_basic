name_list = ['TOM', 'Lily', 'ROSE']

name_list.append([11, 22])   # ====push
print(name_list)  # ['TOM', 'Lily', 'ROSE', [11, 22]]

name_list.append(33)  # ====push
print(name_list)  # ['TOM', 'Lily', 'ROSE', [11, 22], 33]


name_list.extend(['xiaoming', 'xiaohong'])  # 列表合并
print(name_list)  # ['TOM', 'Lily', 'ROSE', [11, 22], 'xiaoming', 'xiaohong']


name_list.insert(1, 'aaa')
print(name_list)  # ['TOM', 'aaa', 'Lily', 'ROSE', [11, 22], 'xiaoming', 'xiaohong']
