in_lst = list(map(str, input().split()))
s_lst = []

for i in in_lst:
    if i in "+-*":
        n = s_lst.pop()
        m = s_lst.pop()
        if i == "+":
            x = n+m
        elif i == "-":
            x = m - n
        else:
            x = n * m
        s_lst.append(int(x))
    else:
        s_lst.append(int(i))
# 配列の前に*をつけると１次元下がった形で出力される
print(*s_lst)
