#　挿入ソート
n = int(input())
n_lst = list(map(int, input().split()))

s_lst = [str(i) for i in n_lst]
print(' '.join(s_lst))
for i in range(1, n):
    v = n_lst[i]
    j = i - 1
    while j >= 0 and n_lst[j] > v:
        n_lst[j+1] = n_lst[j]
        j -= 1
    n_lst[j+1] = v
    s_lst = [str(i) for i in n_lst]
    print(' '.join(s_lst))
