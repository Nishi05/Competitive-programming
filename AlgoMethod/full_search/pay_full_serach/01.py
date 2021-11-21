n, k = map(int, input().split())

a_lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if a_lst[i] + a_lst[j] <= k:
            cnt += 1
print(cnt)
