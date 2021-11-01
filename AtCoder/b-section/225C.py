n, m = map(int, input().split())
mt = [list(map(int, input().split())) for j in range(n)]
flg = True
for i in range(m):
    for j in range(n-1):
        if abs(mt[j][i] - mt[j+1][i]) != 7:
            flg = False
            break
    else:
        continue
    break

if flg:
    print("Yes")
else:
    print("No")
