n, k = map(int, input().split())

n_lst = list(map(int, input().split()))

n_lst.sort(reverse=True)

print(sum(n_lst[:k]))
