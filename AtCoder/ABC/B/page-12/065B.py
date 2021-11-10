
# 配列の長さの中で探索していき、その中で該当の数字が出たら抜ける。
n = int(input())
lst = [int(input()) for _ in range(n)]
a = lst[0]
for i in range(n):
    if a == 2:
        print(i+1)
        break
    a = lst[a-1]
else:
    print(-1)
