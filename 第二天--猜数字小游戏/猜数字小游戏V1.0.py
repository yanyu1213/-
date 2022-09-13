import random

num = int(random.randint(1, 100))
print("一起来玩猜数字小游戏吧！！！"
      "\n游戏规则：请在1-100的范围内进行猜测，否则直接退出游戏，如果猜测数字大了会提示'大了',如果猜测数字小了则会提示'小了'，输入0退出游戏")
while 1:
    a = int(input("请输入数字："))
    if a <= 0 or a >100:
        print("已退出游戏")
        break
    elif a > num:
        print("大了")
    elif a < num:
        print("小了")
    else:
        print(f"恭喜你猜对了，本轮幸运数字为{num}!!!")
