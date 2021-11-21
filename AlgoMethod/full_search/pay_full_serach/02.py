l, r = map(int, input().split())
cnt = 0
for i in range(l, r+1):
    for j in range(i+1, r+1):
        if i % 10 == j % 10:
            cnt += 1
print(cnt)
