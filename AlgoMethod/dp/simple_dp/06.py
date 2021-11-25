n, m = map(int, input().split())
lst = list(map(int, input().split()))

dp = [False]*(n+1)

dp[0] = True

for i in range(1, n+1):
    for j in range(m):
        if i - lst[j] >= 0 and dp[i - lst[j]]:
            dp[i] = True
print("Yes" if dp[n] else "No")
