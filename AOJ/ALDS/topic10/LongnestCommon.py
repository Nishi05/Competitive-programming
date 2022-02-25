n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]
INF = 10**20
dp = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for d in range(1, n):
    for i in range(n - d):
        for j in range(d):
            dp[i][i + d] = min(dp[i][i + d], dp[i][i + j] + dp[i + j + 1]
                               [i + d] + M[i][0] * M[i + j][1] * M[i + d][1])

print(dp[0][n-1])
