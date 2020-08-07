list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 过滤序列中的偶数
def func(x):
    return x % 2 == 0


# 调用filter
result = filter(func, list1)
print(result)
print(list(result))

