x, a, b = map(int, input().split())

if b - a >= x + 1:
    print('dangerous')
else:
    if b - x > 0:
        print('safe')
    else:
        print('delicious')
