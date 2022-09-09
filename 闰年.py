# 输入一个年份判断是不是闰年
a = input("请输入一个年份：")
if a.isdigit():
    a = int(a)
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        print("闰年")
    else:
        print("平年")
else:
    print("请输入正确的年份:")
