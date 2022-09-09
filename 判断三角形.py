# 根据三边判断三角形
a = input("请输入三角形的边：")
b = input("请输入三角形的边：")
c = input("请输入三角形的边：")
if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c >= 0 and a + c > b >= 0 and b + c > a >= 0:
        if (a == b or a == c or b == c) and a != b != c:
            print("等腰三角形")
        elif a == b == c:
            print("等边三角形")
        elif a**a + b**b ==c**c or a**a +c**c == b**b or b**b + c**c ==a**a:
            print("直角三角形")
        elif a**a + b**b > c**c or a**a + c**c > b**b or b**b + c**c > a**a:
            print("锐角三角形")
        elif a**a + b**b < c**c or a**a + c**c < b**b or b**b + c**c > a**a:
            print("钝角三角形")
    else:
        print("请输入正确的数")
