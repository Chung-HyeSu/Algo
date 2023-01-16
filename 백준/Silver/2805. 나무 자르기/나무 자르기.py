#나무 자르기
N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

st = 1
ed = lst[-1]
while st<=ed:
    mid = (st+ed)//2
    cnt = 0
    for i in lst:
        if i>mid:
            cnt += (i-mid)
        if cnt>M:
            break
    if cnt >= M:
        st = mid+1
    else:
        ed = mid-1

print(ed)
