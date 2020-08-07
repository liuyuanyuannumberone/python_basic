name_list = ['TOM', 'Lily', 'ROSE']

'''
1. 准备表示下标数据
2. 循环while
    条件 i < 3  len()
    遍历：依次按顺序访问到序列的每一个数据 
    i += 1
'''
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

for i in name_list:
    # 遍历序列中的数据
    print(i)
name = [['TOM', 'Lily', 'Rose'], ['张三', '李四', '王五'], ['xiaohong', 'xiaoming', 'xiaolv']]
print(name[0][1])






