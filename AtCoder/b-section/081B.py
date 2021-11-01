n = int(input())
list = list(map(int, input().split()))
sum = 0
while 1:
    flg = False
    for i in range(n):
        if list[i] % 2 == 0:
            list[i] = list[i]/2
        else:
            flg = True
            break
    if Flg:
        break
    else:
        sum += 1
print(sum)
