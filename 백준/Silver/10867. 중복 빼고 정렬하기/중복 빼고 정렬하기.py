N = int(input())
arr = list(map(int,input().split()))
arr.sort()

target = 8657303873
for i in range(len(arr)):
    if target != arr[i]:
        target = arr[i]
        print(arr[i])