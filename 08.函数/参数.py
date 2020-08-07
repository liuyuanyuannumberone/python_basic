def user_info(name, age, gender):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')


# 关键字参数之间不分先后顺序
user_info('ROSE', age=20, gender='女')
user_info('小明', gender='男', age=18)
# 位置参数必须写在关键字参数的前面
# user_info(age=20, gender='男', 'TOM')


def user(name, age, gender='男'):
    print(f'您的姓名是{name}, 年龄是{age}, 性别是{gender}')


user('TOM', 18)  # 没有为缺省参数传值，表示使用默认值
user('TOM', 18, gender='女')


# 不定长参数
# 接收所有位置参数，返回一个元组
def userName(*args):
    print(args)


userName('TOM')
userName('TOM', 20)
userName('TOM', 20, 'man')
userName()


# 收集所有关键字参数，返回一个字典
def userId(**kwargs):
    print(kwargs)


userId()
userId(name='TOM')
userId(name='TOM', age=20)