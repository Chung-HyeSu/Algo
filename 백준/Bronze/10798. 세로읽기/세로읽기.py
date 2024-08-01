#10798
arr = []
for i in range(5):
    a = list(input())
    arr.append(a)
    if len(a) < 15:
        while len(a) != 15:
            arr[i].append(0)


for j in range(15):
    for i in range(5):
        if arr[i][j] != 0:
            print(arr[i][j], end='')