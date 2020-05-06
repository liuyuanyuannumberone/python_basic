# 递归特点：函数内部自己调用自己；必须有出口
def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    # 当前数字 + 当前数字-1的累加和
    print(num)
    return num + sum_numbers(num - 1)


result = sum_numbers(2)
print(result)
