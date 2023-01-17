#랜선 자르기
K, N = map(int,input().split())
klst = []
for i in range(K):
    klst.append(int(input()))

st = 1
ed = max(klst)

while st<=ed:
    mid = (st+ed)//2
    cnt = 0
    for i in klst:
        cnt += i//mid
    if cnt >= N :
        st = mid+1
    else:
        ed = mid-1

print(ed)