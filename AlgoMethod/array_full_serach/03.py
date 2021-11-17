n = int(input())
lst = list(map(int, input().split()))

print(sum([1 if i > 0 else 0 for i in lst]))
