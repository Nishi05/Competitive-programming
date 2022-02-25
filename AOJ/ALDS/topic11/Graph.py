n = int(input())
A = [[0]*n for _ in range(n)]

for i in range(n):
    lst = list(map(int, input().split()))
    for j, s in enumerate(lst[1:]):
        if j == 0:
            continue
        else:
            A[i][s-1] = 1

for i in range(n):
    print(*A[i])
