import time
a, b, c, d = map(int, input().split())

a_lst = [False]*100
b_lst = [False]*100

for i in range(a, b):
    a_lst[i] = True
for i in range(c, d):
    b_lst[i] = True
c = 0
for i in range(100):
    if a_lst[i] == True and b_lst[i] == True:
        c += 1
print(c)

# 実験
# 決まった数の範囲を置き換えるときは一回配列を作って、指定の範囲を置き換えた方がいい
# 全体を探す時にはリスト内表記
# import time
# from decimal import Decimal
# a, b, c, d = map(int, input().split())

# t1 = time.time()
# a_lst = [False]*10000
# for i in range(a, b):
#     a_lst[i] = True
# t2 = time.time()

# for i in range(10000):
#     if i >= a and i < b:
#         a_lst[i] = True
#     else:
#         a_lst[i] = False
# t3 = time.time()


# a_lst = [True if i >= a and i < b else False for i in range(10000)]
# t4 = time.time()

# print(Decimal(t2 - t1))
# print(t3 - t2)
# print(t4 - t3)
