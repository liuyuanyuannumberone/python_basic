age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

print('年龄%d岁' % age)  # 年龄18岁 -- 整数 %d
print('我的学号是%03d' % stu_id)  # 我的学号是001
print('我的学号是%03d' % stu_id2)  # 我的学号是1000  超出的原样输出

print('体重是%.2f公斤' % weight)  # 体重是75.50公斤 -- 浮点数 %f
print('名字%s' % name)  # 名字TOM -- 字符串 %s

print('我的名字是%s，今年%d岁了' % (name, age))
print('我的名字是%s，明年%d岁了' % (name, age + 1))

print(f'我的名字是{name}，今年{age}岁了')  # f'{表达式}'

print('hello\nPython')
print('\tabcd')  # 一个tab键4个空格的距离

print('hello', end="\n")  # print默认有\n
print('world', end="\t\t")
print('hello', end="...")
print('Python')
