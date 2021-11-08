n = int(input())
t_lst = []
k_lst = []
a_grand_lst = []
need = [False]*n
need[-1] = True
for i in range(n):
    t, k, *a_lst = map(int, input().split())
    t_lst.append(t)
    k_lst.append(k)
    a_grand_lst.append(a_lst)

for i in range(n-1, 0, -1):
    if need[i]:
        for j in a_grand_lst[i]:
            print(a_grand_lst)
            print(j)
            j -= 1
            need[j] = True

print(sum([t_lst[i] for i in range(n) if need[i]]))
