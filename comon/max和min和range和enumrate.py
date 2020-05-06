str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]

# max() : 最大值
print(max(str1))
print(max(list1))

# min() ： 最小值
print(min(str1))
print(min(list1))

print("=================")
# range(start, end, step)
# 1. 如果不写开始，默认从0开始
# 2. 如果不写步长，默认为1
print(range(1, 10, 1))  # range(1, 10)
for i in range(1, 10, 1):
    print(i)

# for i in range(1, 10):
#     print(i)

# for i in range(10):
#    print(i)

print("------------------------")
list1 = ['a', 'b', 'c', 'd', 'e']

# enumerate 返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
for i in enumerate(list1):
     print(i)

for i in enumerate(list1, start=1):
    print(i)
