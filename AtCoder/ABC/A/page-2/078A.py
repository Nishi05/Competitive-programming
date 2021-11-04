# asciiコード変換では 文字->数字 = ord() 数字->文字 = chr()
a, b = map(str, input().split())
if a == b:
    print("=")
elif ord(a) < ord(b):
    print("<")
else:
    print(">")
