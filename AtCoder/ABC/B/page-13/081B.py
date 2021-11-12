# 黒板に N 個の正の整数 A_1 ,...,A_N
# が書かれています．
# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
# 黒板に書かれている整数すべてを，2 で割ったものに置き換える．
# すぬけ君は最大で何回操作を行うことができるかを求めてください．

n = int(input())
a = list(map(int, input().split()))
cnt = 0
# 一番初めに全部偶数だった場合に＋１するため
flg = True
while 1:
    for i in range(n):
        if (a[i]/2) % 2 != 0:
            break
        else:
            a[i] = a[i]/2
    else:
        if flg:
            cnt += 1
            flg = False
        cnt += 1
        continue
    break

print(cnt)
