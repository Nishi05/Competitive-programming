n = int(input())
list = list(map(int, input().split()))
nlist = []
for i in range(n-1, 0, -1):
    # print(i)
    nlist.append(list[i])

print(" ".join(map(str, nlist)))
