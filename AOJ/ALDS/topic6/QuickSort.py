N = int(input())
A = [[0]*2 for _ in range(N)]

for i in range(N):
    s, n = map(str, input().split())
    A[i][0] = s
    A[i][1] = int(n)


def partition(p, r):
    x = A[r][1]
    i = p
    for j in range(p, r):
        if A[j][1] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)


A_stable = sorted(A, key=lambda x: x[1])
quick_sort(0, N-1)

if all(A[i][0] == A_stable[i][0] for i in range(N)):
    print("Stable")
else:
    print("Not stable")

for a in A:
    print(*a)
