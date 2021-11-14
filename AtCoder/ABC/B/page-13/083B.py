n, a, b = map(int, input().split())

ans = 0
for i in range(n+1):
    cnt = 0
    for j in str(i):
        cnt += int(j)
    if a <= cnt <= b:
        ans += i
print(ans)
