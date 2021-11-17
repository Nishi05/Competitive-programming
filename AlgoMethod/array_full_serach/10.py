n = int(input())
lst = list(map(int, input().split()))
n_lst = [0]*9

for i in range(n):
    n_lst[lst[i]-1] += 1

print(n_lst.index(max(n_lst))+1)
