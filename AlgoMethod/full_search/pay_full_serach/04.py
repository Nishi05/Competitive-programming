n = int(input())
lst = [str(input()) for _ in range(n)]

print("Yes") if len(sorted(set(lst), key=lst.index)) != len(lst) else print("No")
