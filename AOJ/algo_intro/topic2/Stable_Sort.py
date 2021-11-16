# 安定ソート
n = int(input())
b_lst = list(map(str, input().split()))
s_lst = b_lst[:]


def bubblesort(lst, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if lst[j][1] < lst[j - 1][1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst


def selectionsort(lst, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if lst[j][1] < lst[minj][1]:
                minj = j
        lst[i], lst[minj] = lst[minj], lst[i]
    return lst


print(' '.join([str(i) for i in bubblesort(b_lst, n)]))
print('Stable')
print(' '.join([str(i) for i in selectionsort(s_lst, n)]))
print('Stable') if bubblesort(b_lst, n) == selectionsort(
    s_lst, n) else print('Not stable')
