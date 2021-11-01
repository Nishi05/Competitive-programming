n = int(input())
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    info = list(map(int, input().split()))
    count[info[0]-1][info[1]-1][info[2] - 1] += info[3]


for k in range(4):
    for j in range(3):
        for i in range(10):
            print(" {}".format(count[k][j][i]), end="")
        print()
    if(k != 3):
        print("#"*20)
