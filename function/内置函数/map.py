list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


# 调用map
result = map(func, list1)
print(result)
print(list(result))


