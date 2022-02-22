n = int(input())
A = list(map(int, input().split()))
sortA = sorted(A)

ans = 0
for i in range(n):
    x = A.index(sortA[i])
    j = 0
    while x > i:
        j += 1
        y = A.index(sortA[x])
        ans += A[y]
        A[x], A[y] = A[y], A[x]
        x = y
    ans += min(sortA[i] * j, sortA[i] * 2 + sortA[0] * (j + 2))

print(ans)
