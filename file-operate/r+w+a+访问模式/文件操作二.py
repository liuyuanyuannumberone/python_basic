"""
r+: 读写文件     文件不存在报错
w+: 读写文件      文件存在覆盖 文件不存在则创建
a+：读写文件     文件存在则追加，文件不存在则创建
b 为二进制
"""
"""
r  rb   r+  rb+ 
w  wb   w+  wb+ 
a  ab   a+  ab+ 

+  代表可读写
b  表示二进制
r/w/a  
r 表示文件不存在报错，文件指针在开头
w 表示文件存在则覆盖，不存在则创建 ，文件指针在开头 
a 表示文件存在则追加，不存在则创建，文件指针在结尾

"""

f1 = open('txt/readline.txt', 'r+')
print(f1.read())
f1.close()

print("===")
f2 = open('txt/readline.txt', 'a+')
print(f2.read())
f2.close()
print("===")

