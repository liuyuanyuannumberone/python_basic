"""
函数先定义后调用
"""


def add_num2(a, b):
    add_result = a + b
    return add_result


result = add_num2(10, 20)
print(result)


def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


help(sum_num1)  # 查看函数的说明文档(函数的解释说明的信息)
