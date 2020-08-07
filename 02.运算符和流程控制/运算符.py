a = 10
a += 1  # a = a + 1
print(a)  # 11

# 注意： 先算复合赋值运算符右面的表达式；
c = 10
c += 1 + 2
print(c)  # 13

d = 10
d *= 1 + 2
print(d)   # 30


aa = 0
bb = 1
cc = 2
# and or not
print((aa < bb) and (cc > bb)) # True
print((aa < bb) or (cc > bb))    # True
print(not False)  # True
print(not cc < bb)  # True


