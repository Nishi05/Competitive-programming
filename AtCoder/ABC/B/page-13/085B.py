n = int(input())

k_lst = [int(input()) for _ in range(n)]
k_lst.sort(reverse=True)
cnt = 1
for i in range(n-1):
    if k_lst[i] == k_lst[i+1]:
        continue
    if k_lst[i] > k_lst[i+1]:
        cnt += 1
print(cnt)
