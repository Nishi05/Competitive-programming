# 英小文字のみからなる文字列 s, t が与えられます。 あなたは、s の文字を好きな順に並べ替え、文字列 s′を作ります。
# また、t の文字を好きな順に並べ替え、文字列 t′を作ります。
# このとき、辞書順で s′< t′
# となるようにできるか判定してください。

s = list(map(str, input()))
t = list(map(str, input()))
s.sort()
t.sort(reverse=True)

if ''.join(s) < ''.join(t):
    print('Yes')
else:
    print('No')
