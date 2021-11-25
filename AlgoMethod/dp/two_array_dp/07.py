n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
INF = 1000000
dp = [[INF]*n for _ in range(n)]
dp[0][n-1] = lst[0][n-1]

for i in range(n):
    for j in range(n-1, -1, -1):
        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + lst[i][j])
        if j + 1 < n:
            dp[i][j] = min(dp[i][j], dp[i][j+1] + lst[i][j])
print(dp[n-1][0])
