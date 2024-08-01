#2490 윷놀이
yoot = 'ABCDE'
for i in range(3):
    arr = list(map(int,input().split()))
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            cnt +=1
    print(yoot[cnt-1])