# 5の数と7の数が合っていればいいので、mapで取るのではなくlistでとって、対象の数を数える

list = list(map(int, input().split()))
seven = 0
five = 0
for i in list:
    if i == 7:
        seven += 1
    elif i == 5:
        five += 1
if seven == 1 and five == 2:
    print("YES")
else:
    print("NO")
