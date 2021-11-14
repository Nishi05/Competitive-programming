a, b = map(int, input().split())
s_lst = list(map(str, input().split('-')))

if len(s_lst[0]) == a and len(s_lst[1]) == b:
    print('Yes')
else:
    print('No')
