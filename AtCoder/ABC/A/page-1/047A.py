# パックからキャンディーは取り出せないので、必ずパックは2-1になる。
# なので、パック1つのキャンディーの数 = パック2つのキャンディーの数
a, b, c = map(int, input().split())

if a == b + c or b == c + a or c == a + b:
    print("Yes")
else:
    print("No")
