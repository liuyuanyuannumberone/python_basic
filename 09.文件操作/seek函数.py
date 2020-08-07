"""
用来移动文件指针
文件对象.seek(偏移量, 起始位置)     0开头 1当前 2结尾
"""

f = open('txt/test.txt', 'r+')
print("==")
f.seek(5,0)
print(f.read())
f.close()

print("==")

f1 = open('txt/test.txt', 'a+')
print("==")
f1.seek(0,0)
print(f1.read())
f1.close()

