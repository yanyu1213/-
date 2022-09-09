# 根据角度判断三角形
a = input("请输入三角形的角度：")
b = input("请输入三角形的角度：")
c = input("请输入三角形的角度：")
if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b + c == 180:
        if a == 90 or b == 90 or c == 90:
            print("直角三角形")
        elif a < 90 and b < 90 or c < 90:
            print("锐角三角形")
        elif a > 90 or b > 90 or c > 90:
            print("钝角三角形")
    else:
        print("输入的三角形不符合三角形构成，请输入正确的数：")
