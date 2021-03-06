# ある合宿におやつとしてチョコレートが何個か準備されました。 合宿は N 人が参加して D 日間行われました。 i 人目の参加者 (1≤i≤N) は合宿の 1,A_i+1,2A_i+1,...
# 日目にチョコレートを 1 個ずつ食べました。 その結果、合宿終了後に残っていたチョコレートは X 個となりました。
# また、合宿の参加者以外がチョコレートを食べることはありませんでした。
# 合宿開始前に準備されていたチョコレートの個数を求めてください。

n = int(input())
d, x = map(int, input().split())
cnt = n + x
for _ in range(n):
    m = int(input())
    if m == 1 or d % m == 0:
        cnt -= 1
    cnt += d//m
print(cnt)
