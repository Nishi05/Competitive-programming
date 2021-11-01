r, c = map(int, input().split())

m = [[] for i in range(c)]

for i in range(r):
    m[i] = list(map(int, input().split()))

for i in range(r):
    sum = 0
    for j in range(c):
        sum += m[i][j]
        print(m[i][j], end=" ")
        if(j == c-1):
            print(sum, end=" ")
    print()
