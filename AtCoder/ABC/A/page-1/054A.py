# 1の数が来たら、足し算をして13より大きくする
a, b = map(int, input().split())

if a == 1:
    a += 13
if b == 1:
    b += 13
if a == b:
    print('Draw')
elif a < b:
    print('Bob')
else:

    print('Alice')
