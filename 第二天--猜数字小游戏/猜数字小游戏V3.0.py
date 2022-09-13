import random

num = int(random.randint(1, 100))
a = 5000
print("一起来玩猜数字小游戏吧！！！"
      "\n游戏规则：请在1-100的范围内进行猜测，否则直接退出游戏，如果猜测数字大了会提示'大了',如果猜测数字小了则会提示'小了'，输入0退出游戏")
while 1:
    b = int(input("请输入数字："))
    if b <= 0 or a == 500 or b > 100:
        print("已退出游戏")
        break
    elif b > num:
        print("大了")
        a = a - 500
        print(f"余额:{a}金币")
    elif b < num:
        a = a - 500
        print("小了")
        print(f"余额:{a}金币")
    else:
        a = a + 3000
        print(f"恭喜你猜对了，本轮幸运数字为{num}!!!")
        print(f"余额:{a}金币")
        c = int(input("是否继续游戏（输入666继续）："))
        if c == 666:
            num = int(random.randint(1, 100))
        else:
            break
