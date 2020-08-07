"""
 input接收到的数据类型都是字符串
"""
password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password))  # <class 'str'>


num = input('请输入数字：')
numInt = int(num)
print(type(numInt))  # int
