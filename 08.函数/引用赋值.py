# python中值是靠引用来传递的

# 不可变：int：id()检测两个变量的id值(内存的十进制值),判断两个变量是否为同一个值的引用，id值为内存中的地址标识
a = 1
b = a
print(id(a))  # 140720324269728
print(id(b))

# 因为修改了a的数据，内存要开辟另外一份内存取存储2，id检测a和b的地址不同
a = 2
print(id(a))
print(id(b))

print("===========")

# 可变类型：列表
aa = [10, 20]
bb = aa
print(id(aa))
print(id(bb))  # 一样

aa.append(30)
print(aa)  # 一样
print(bb)  # 一样

print(id(aa))  # 一样
print(id(bb))  # 一样

"""
 调用函数 -- 把可变和不可变两种类型依次当做实参传入
"""


def test1(a):
    print(a)  # 100
    print(id(a))  # 400

    a += a
    print(a)  # 200
    print(id(a))  # 600


b = 100
test1(b)

print("=======")
c = [11, 22]
test1(c)
