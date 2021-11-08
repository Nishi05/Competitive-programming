# 割る数と足していく倍数を掛けた数まで見ていくといい。
# なぜか？- そこを超えると同じあまりの数になるから

a, b, c = map(int, input().split())
for i in range(1, b + 1):
    if a * i % b == c:
        print("YES")
        break
else:
    print("NO")
