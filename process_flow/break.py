i = 1
while i <= 5:
    if i == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1

print("==========")
i = 1
while i <= 5:
    if i == 3:
        print('吃出一个大虫子，这个苹果不吃了')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
