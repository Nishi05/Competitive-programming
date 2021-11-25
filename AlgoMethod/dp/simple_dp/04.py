n = int(input())

F = [0]*(n+1)

F[0] = 1

for i in range(1, n+1):
    if i - 1 >= 0:
        F[i] += F[i-1]
    if i - 2 >= 0:
        F[i] += F[i-2]
    if i - 3 >= 0:
        F[i] += F[i-3]
print(F[n])
