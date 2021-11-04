# list型にして、join関数で文字列を作成
list = list(map(str, input().split()))
s = ''.join(list)

print('YES') if int(s) % 4 == 0 else print('NO')
