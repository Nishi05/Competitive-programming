n, k = map(int, input().split())

lst = [input().split()for _ in range(n)]
print(lst)
sum_lst = [sum(int(*i)) for i in lst]
print(sum_lst)
# for i in range(n):
