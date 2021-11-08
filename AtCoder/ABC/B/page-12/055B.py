# for文の回す回数に着目するのではなく、１回の計算量を小さくする
import time
n = int(input())
t1 = time.time()
x = 1
for i in range(1, n+1):
    x = (i * x) % (10**9 + 7)

print(x)
t2 = time.time()

print(t2 - t1)
