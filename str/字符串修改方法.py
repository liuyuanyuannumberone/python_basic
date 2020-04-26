mystr = "hello world and itcast and itheima and Python"

# replace(旧字串，新字串，替换次数) 把and换成he
# 原有字符串的数据并没有做到修改,返回值是修改后的字符串
new_str = mystr.replace('and', 'he')
print(new_str)

new_one = mystr.replace('and', 'he', 1)
print(new_one)

# 数据是否可以改变划分为 可变类型 和 不可变类型


#  split(分割字符，分割字符出现的此时) 返回一个列表, 丢失分割字符
list1 = mystr.split('and')
list2 = mystr.split('and', 2)
print(list1)  # ['hello world ', ' itcast ', ' itheima ', ' Python']
print(list2)  # ['hello world ', ' itcast ', ' itheima and Python']

# join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']
new_str = '...'.join(mylist)
print(new_str)  # aa...bb...cc

#  capitalize() 字符串首字母大写
str1 = "hello world and itcast and itheima and Python"
str2 = str1.capitalize()
print(str2)  # Hello world and itcast and itheima and python

# title(): 字符串中每个单词首字母大写
str3 = str1.title()
print(str3)  # Hello World And Itcast And Itheima And Python

# upper()：小写转大写
str4 = str1.upper()
print(str4)  # HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON

# lower(): 大写转小写
str5 = str1.lower()
print(str5)  # hello world and itcast and itheima and python

str6 = "   hello world and itcast and itheima and Python   "
#  lstrip(): 删除左侧空白字符
str7 = str6.lstrip()
print(str7)

#  rstrip(): 删除右侧空白字符
str8 = str6.rstrip()
print(str8)

# strip()：删除两侧空白字符
str9 = str6.strip()
print(str9)

my = 'he'
# ljust(长度，填充字符) 返回一个左对齐的字符串，并使用指定字符（默认为空格）填充至对应长度的新字符串
# rjust center
aa = my.ljust(5, 'a')
print(aa)  # heaaa

