"""
r 只读     文件不存在报错
w 只写     文件存在首先覆盖 文件不存在则创建
a 追加     文件存在则追加，文件不存在则创建

"""

f = open('txt/write.txt', 'w')  # 写入
f.write('write')
f.close()


# 文件内容如果换行，底层有\n，会有字节占位，导致read书写参数读取出来的眼睛看到的个数和参数值不匹配
# read不写参数表示读取所有；
f1 = open('txt/read.txt', 'r')  # 只读
# print(f1.read())
print(f1.read(10))  # 代表的是字节
f1.close()

# 追加
f2 = open('txt/append.txt', 'a')
f2.write('append \n')
f2.close()