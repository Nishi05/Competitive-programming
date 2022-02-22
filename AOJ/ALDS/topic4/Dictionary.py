N = int(input())
s = set()
ans = []
for _ in range(N):
    cmd, dict = map(str, input().split())
    if cmd == 'insert':
        s.add(dict)
    elif cmd == 'find':
        if dict in s:
            ans.append('yes')
        else:
            ans.append('no')
for j in ans:
    print(j)
