n = int(input())


def cnt_digit(N):
    return len(str(N))


ans = cnt_digit(n)
A = 1
while 1:
    if A * A > n:
        break
    if n % A != 0:
        A += 1
        continue
    B = n/A
    cur = max(cnt_digit(A), cnt_digit(int(B)))
    if ans > cur:
        ans = cur
    A += 1

print(ans)
