# 2次配列で格納して、学生(i)を基準に各チェックポイント(m)とのマンハッタン距離を見ていく
# dis_lstに格納し、一番小さかった数字が格納されている配列番号を取ってくる。その番号に+1をし各チェックポイントの番号として、表示する。
# https://note.nkmk.me/python-list-index/
n, m = map(int, input().split())

s_lst = [list(map(int, input().split())) for _ in range(n)]
c_lst = [list(map(int, input().split())) for _ in range(m)]
dis_lst = []
min_lst = []

for i in range(0, n):
    for j in range(0, m):
        dis = abs(s_lst[i][0] - c_lst[j][0]) + \
            abs(s_lst[i][1] - c_lst[j][1])
        dis_lst.append(dis)
    min_lst.append(dis_lst.index(min(dis_lst)) + 1)
    dis_lst = []

for i in range(n):
    print(min_lst[i])
