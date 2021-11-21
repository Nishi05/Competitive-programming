n = int(input())

lst = list(map(int, input().split()))
cnt = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if max(lst[i], lst[j], lst[k]) == lst[j]:
                cnt += 1
print(cnt)
