# aの中にbは含まれるかを考える
# aがn*n bがm*mだった場合探索すべき箇所は、n-m+1
# 画素が同じ場合を見つけるために、nの中を動かしながら、mにあった文字列を見つける。合うを確認するために配列を縦でみている
n, m = map(int, input().split())
a = [str(input()) for _ in range(n)]
b = [str(input()) for _ in range(m)]

exist = False
for lx in range(n-m+1):
    for ly in range(n-m+1):
        match = True
        for x in range(m):
            for y in range(m):
                if a[ly+y][lx+x] != b[y][x]:
                    match = False

        if match:
            exist = True

print("Yes") if exist else print("No")
