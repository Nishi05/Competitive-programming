# https://atcoder.jp/contests/abc227/editorial/2906
# 最後のcntではCが取りうる値の実行回数を足している
n = int(input())
cnt = 0
for i in range(1, n+1):
    if i**3 > n:
        break
    for j in range(i, n+1):
        if i*j*j > n:
            break
        cnt += n//i//j-j+1
print(cnt)
