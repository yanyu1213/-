# 输入身高和体重，计算BMI判断健康状态
a = float(input("请输入身高:  m:"))
b = float(input("请输入体重:  kg"))
c = b / (a ** a)
s = '你的健康状态:%s'
if a > 0 and b > 0:
    if c < 18.5:
        print(s % "轻体重")
    if 18.5 <= c <= 24:
        print(s % "健康体重")
    if 24 <= c <= 28:
        print(s % "超重")
    if 28 <= c:
        print(s % "肥胖")
else:

    print("请输入正确的数：")
