"""
 input接收到的数据类型都是字符串
"""
num = input('请输入：')
print(f'您输入的密码是{num}')
print(type(num))  # <class 'str'>
numInt = int(num)
print(type(numInt))  # int
