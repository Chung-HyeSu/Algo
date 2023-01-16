#숫자 카드 2
N = int(input())
nlst = list(map(int,input().split()))
nlst.sort()
M = int(input())
mlst = list(map(int,input().split()))

#1. nlst 각 요소의 갯수를 셈
cnt = {}
for i in nlst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

#2. mlst 각 요소가 cnt에 있는지 확인
for i in mlst:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')