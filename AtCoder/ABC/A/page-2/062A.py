# 配列の中身をグループ番号にして、入力値を配列の参照先にするという回答
x, y = map(int, input().split())
a = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
s = 'Yes' if a[x] == a[y] else 'No'
print(s)

# x, y = map(str, input().split())
# if x in ['1', '3', '5', '7', '8', '10', '12'] and y in ['1', '3', '5', '7', '8', '10', '12']:
#     print('Yes')
# elif x in ['4', '6', '9', '11'] and y in ['4', '6', '9', '11']:
#     print('Yes')
# else:
#     print('No')
