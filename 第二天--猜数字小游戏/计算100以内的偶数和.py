# 第一种
sum = 0
for i in range(0, 101, 2):
    sum = sum + i
print(sum)
# 第二种
sum = 0
i = 0
while i <= 100:
    sum = sum + i
    i += 2
print(sum)
