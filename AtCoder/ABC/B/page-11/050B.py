n = int(input())
p_lst = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    tamp = p_lst[a-1]
    p_lst[a-1] = b
    print(sum(p_lst))
    p_lst[a-1] = tamp
