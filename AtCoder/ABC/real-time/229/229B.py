a, b = map(str, input().split())

m = abs(len(b) - len(a))
if len(a) == len(b):
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) >= 10:
            print('Hard')
            break
    else:
        print('Easy')
elif len(a) > len(b):
    for i in range(len(b)-1, -1, -1):
        if int(a[i+m]) + int(b[i]) >= 10:
            print('Hard')
            break
    else:
        print('Easy')
else:
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i+m]) >= 10:
            print('Hard')
            break
    else:
        print('Easy')
