N = int(input())
nlst = list(map(int,input().split()))
nlst.sort()
M = int(input())
mlst = list(map(int,input().split()))


def binary(i):
    st = 0
    ed = N-1
    while st<=ed:
        mid = (st+ed)//2
        if nlst[mid] == i:
            return True
        elif nlst[mid] > i:
            ed = mid-1
        elif nlst[mid] < i:
            st = mid+1


for i in range(M):
    if binary(mlst[i]):
        print(1)
    else:
        print(0)
