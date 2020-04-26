mystr = "hello world and itcast and itheima and Python"

#  find(字串，开始位置的下标，结束位置的下标)  检测子穿串是否包含在字符串中，如果在返回这个字串的下标，否则返回-1
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # -1 , ands子串不存在

# index()字串，开始位置的下标，结束位置的下标  测子穿串是否包含在字符串中，如果在返回这个字串的下标，否则返回异常
print(mystr.index('and'))  # 12
print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # 如果index查找子串不存在，报错

# count() 返回字串在字符串中出现的次数
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # 0

# rfind() 和find功能相同，他是从右侧开始查
print(mystr.rfind('and'))
print(mystr.rfind('ands'))

# rindex() 和index功能相同，他是从右侧开始查
print(mystr.rindex('and'))
# print(mystr.rindex('ands'))



test = "hello world and itcast and itheima and Python"
# startswith(字串，开始位置下标，结束位置下标): 判断字符串是否以某个子串开头
print(test.startswith('hello'))  # True
print(test.startswith('he'))  # True

# endswith(): 判断字符串是否以某个子串结尾
print(test.endswith('on'))  # True

#  isalpha(): 字母  所有字符都是字母
print(test.isalpha())  # False
# isdigit(): 数字    所有字符都是数字
print(test.isdigit())  # False

# isalnum() : 所有字符都是字母或者数字
print(test.isalnum())  # False
# isspace(): 空白 字符串中只包含空白返回True
print(test.isspace())  # False
