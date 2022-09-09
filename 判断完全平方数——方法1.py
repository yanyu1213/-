# 判断完全平方数
a = input("请输入你要判断是数：")
a = int(a)
b = a**0.5
if b-int(b) == 0:
    print("你输入的数是完全平方数")
else:
    print("您输入的数不是完全平方数")
