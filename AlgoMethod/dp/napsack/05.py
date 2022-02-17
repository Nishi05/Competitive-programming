N, M = map(int, input().split())

W = list(map(int, input().split()))
INF = 10000000
dp = [[INF]*(M+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == INF:
            continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        if j + W[i] <= M:
            dp[i+1][j+W[i]] = min(dp[i][j+W[i]], dp[i][j]+1)


print(dp[N][M] if dp[N][M] != INF else -1)
