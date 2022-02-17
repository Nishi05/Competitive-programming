def main():
    S = str(input())
    n = len(S)
    next = calcNext(S)
    # print(res)
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(n):
        for j in range(26):
            if next[i][j] >= n:
                continue
            dp[next[i][j]+1] = add(dp[next[i][j]+1], dp[i])
    res = 0
    for i in range(n+1):
        res = add(res, dp[i])
    print(next)
    print(res)
    print(dp)


def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a


def calcNext(S):
    n = len(S)
    res = [[n]*26 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(26):
            res[i][j] = res[i+1][j]
        # print(res[i][ord(S[i]) - ord('a')])
        res[i][ord(S[i]) - ord('a')] = i
    return res


if __name__ == "__main__":
    MOD = 1000000007
    main()
