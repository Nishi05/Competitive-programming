n = int(input())
flg = True
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            print("Yes")
            flg = False
            break
    else:
        continue
    break

if flg:
    print("No")
