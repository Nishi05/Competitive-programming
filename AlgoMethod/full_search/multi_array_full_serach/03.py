n, m, k = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))
cnt = 0
for i in a_lst:
    for j in b_lst:
        for k in c_lst:
            if i + j == k:
                cnt += 1
print(cnt)
