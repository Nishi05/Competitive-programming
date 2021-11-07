s = list(map(str, input()))
s.sort()
m = "".join(s)
print("Yes") if m == "abc" else print("No")
