import os

flag = int(input('请输入：'))

file_list = os.listdir()
path = os.getcwd()
# print(file_list)  # ['批量重命名.py']
# print(path)

num = 1
new_name = ''
for name in file_list:
    if name == '批量重命名':
        break
    if flag == 1:
        new_name = '00' + str(num) + name
    elif flag == 2:
        index = 2 + len(str(num))
        new_name = name[index:]
    os.rename(name, new_name)
    num += 1

os.chdir(path)
