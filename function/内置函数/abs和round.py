# abs(): 绝对值
# round()： 四舍五入


# print(abs(-10))
# print(round(1.2))
# print(round(1.9))


# 高阶函数:f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)


result1 = sum_num(-1, 5, abs)
print(result1)

result2 = sum_num(1.1, 1.3, round)
print(result2)
