age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
else:
    print(f'您输入的年龄是{age},小朋友，回家写作业去')

if age < 18:
    print(f'您输入的年龄是{age}, 童工')
elif (age >= 18) and (age <= 60):
    print(f'您输入的年龄是{age}, 合法')
elif age > 60:
    print(f'您输入的年龄是{age}, 退休年龄')


money = 0
seat = 1
if money == 1:
    print('土豪，请上车')
    if seat == 1:
        print('有空座，坐下了')
    else:
        print('没有空座，站着等....')
else:
    print('朋友，没带钱，跟着跑，跑快点')


# 需求： 有两个变量，比较大小 如果变量1 大于 变量2 执行 变量 1 - 变量2； 否则 变量2 - 变量1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)