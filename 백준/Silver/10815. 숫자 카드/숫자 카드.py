#숫자카드
N = int(input())
nlst = list(map(int,input().split()))
M = int(input())
mlst = list(map(int,input().split()))
nlst.sort()


def binary(t):
    st = 0
    ed = N-1
    result = 0
    while st<=ed:
        mid = (st+ed)//2
        if nlst[mid] == t:
            result = 1
            break
        elif nlst[mid] < t:
            st = mid + 1
        elif nlst[mid] > t:
            ed = mid -1
    print(result, end=' ')


for m in mlst:
    binary(m)