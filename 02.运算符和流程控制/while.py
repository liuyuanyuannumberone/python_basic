i = 1
while i <= 3:
    print('媳妇儿，我错了')
    i += 1

m = 1
result = 0
while m <= 100:
    if m % 2 == 0:
       result += m
    m += 1
print(result)

j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i*j}', end='\t')
        i += 1
    # 一行的表达式结束
    print()
    j += 1
