n, k = map(int, input().split())
all = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == k:
        all += 1
print(all)
