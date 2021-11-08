# xとyを決めると、自動的にzが決まる。そして、zが0以上でk以下だと、
# x + y + z = s が成立するので数える。
# 3変数あったときに、2変数でもう一つの変数が決定できることを考える
k, s = map(int, input().split())

count = 0
for i in range(k+1):
    for j in range(k+1):
        z = s - i - j
        if 0 <= z and z <= k:
            count += 1

print(count)
