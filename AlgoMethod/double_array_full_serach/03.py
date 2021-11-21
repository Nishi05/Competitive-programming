l, r = map(int, input().split())
cnt = 0
for i in range(l, r+1):
    m = str(i)[::-1]
    if str(i) == str(m):
        cnt += 1
print(cnt)
