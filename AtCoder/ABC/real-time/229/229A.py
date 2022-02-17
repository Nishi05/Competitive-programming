n = str(input())
m = str(input())

if n == '##':
    print('Yes')
elif n == '.#':
    if m == '#.' or m == '..':
        print('No')
    else:
        print('Yes')
elif n == '#.':
    if m == '.#' or m == '..':
        print('No')
    else:
        print('Yes')
else:
    if m == '##':
        print('Yes')
    else:
        print('No')
