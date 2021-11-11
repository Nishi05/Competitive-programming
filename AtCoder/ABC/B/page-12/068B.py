# 最高が100なので全探索をしても間に合う
# 2で割れる回数を計算する時は、whileを使って2で割った時に余りが0だった場合は
# 2で割って回数を計算することで実現できる
n = int(input())
lst = [0]*n
mac = -1
ans = -1
for i in range(1, n+1):
    c = 0
    y = i
    while y % 2 == 0:
        y /= 2
        c += 1
    if mac < c:
        mac = c
        ans = i
print(ans)
