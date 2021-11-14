n = int(input())

lst = list(map(str, input().split()))

print('Four') if lst.count('Y') != 0 else print('Three')
