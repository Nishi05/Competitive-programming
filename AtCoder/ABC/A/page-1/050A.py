# str型でとってきて、opで条件分岐しながらint型に直して計算
a, b, c = map(str, input().split())

if b == '+':
    print(int(a)+int(c))
else:
    print(int(a)-int(c))
