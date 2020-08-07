old_name = input('请输入您要备份的文件名：')
index = old_name.rfind('.')  # 提取后缀 5
postfix = ''
if index > 0:
    postfix = old_name[index:]
new_name = old_name[:index] + '-bak' + postfix   # 字段串切片

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 文件过大容易卡死，电脑一次性不能读容量很大的文件
# 需要循环读取
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

old_f.close()
new_f.close()

