def lcs(X, Y):
    L = [0] * (len(Y) + 1)
    for x in X:
        l_pre = L[:]
        for j, y in enumerate(Y):
            if x == y:
                L[j+1] = l_pre[j] + 1
            elif L[j+1] < L[j]:
                L[j+1] = L[j]
    return L[-1]


for _ in range(int(input())):
    print(lcs(input(), input()))
