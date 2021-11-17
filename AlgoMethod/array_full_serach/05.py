n = int(input())
lst = list(map(int, input().split()))

print(sum([1 if lst[i] < lst[i+1] else 0 for i in range(n-1)]))
