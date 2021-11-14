# 高橋君は青いカードを N 枚，赤いカードを M 枚持っています。 カードにはそれぞれ文字列が書かれており， i 枚目の青いカードに書かれている文字列は s_i，
# i 枚目の赤いカードに書かれている文字列は t_iです。
# 高橋君は，文字列を 1 つ言います。 そして，全てのカードを確認し， その文字列が書かれた青いカードを 1 枚見つけるごとに 1 円貰えます。
# また，その文字列が書かれた赤いカードを 1 枚見つけるごとに 1 円失います。
# シンプルに全探索で実装する。ある値を決めてb_lstにあるなら+1、r_lstなら-1をしてmaxの値を取得する
n = int(input())
b_lst = [str(input()) for _ in range(n)]
m = int(input())
r_lst = [str(input()) for _ in range(m)]
ans = 0
for i in range(n):
    point = 0
    for x in range(n):
        if b_lst[x] == b_lst[i]:
            point += 1
    for x in range(m):
        if r_lst[x] == b_lst[i]:
            point -= 1
    ans = max(ans, point)
print(ans)
