# 配列の周辺を調べるときに、該当配列からさらにfor文を使って、周りの配列を参照する。
# その時に、参照先が範囲を超えないように0以上や幅や高さ以内という調整する。
h, w = map(int, input().split())
mt = [list(map(str, input())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if mt[i][j] == '#':
            continue
        bb = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                dx = i + x
                dy = j + y
                if 0 <= dx <= h - 1 and 0 <= dy <= w - 1:
                    if mt[dx][dy] == "#":
                        bb += 1
        mt[i][j] = str(bb)

for s in mt:
    print(''.join(s))
