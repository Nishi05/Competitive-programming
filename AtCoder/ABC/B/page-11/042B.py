n, l = map(int, input().split())

list = [str(input()) for i in range(n)]

list.sort()

s = ''.join(list)

print(s)
