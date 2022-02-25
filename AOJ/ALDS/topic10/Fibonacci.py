n = int(input())
dp = [-1]*50


def fib(n):
    if n == 0 or n == 1:
        dp[n] = 1
        return dp[n]
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n - 1) + fib(n - 2)
        return dp[n]


print(fib(n))
