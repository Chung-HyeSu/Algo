#영역 구하기
from collections import deque
M,N,K = map(int,input().split()) #y,x 좌표
arr = [[0]*N for _ in range(M)]
used = [[0]*N for _ in range(M)]

#1. 점찍기
for _ in range(K):
    a,b,c,d = map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            arr[i][j] = 1

#2. 영역 세기
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used[y][x] = 1
    cnt = 1

    while q:
        now = q.popleft()
        y,x = now[0], now[1]
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i]+y
            dx = directx[i]+x
            if dy<0 or dx<0 or dy>=M or dx>=N: continue
            if arr[dy][dx] == 1 : continue
            if arr[dy][dx] == 0 and used[dy][dx] == 0:
                used[dy][dx] = 1
                q.append([dy,dx])
                cnt += 1
    return cnt


result = []
chance = 0
for k in range(M):
    for l in range(N):
        if arr[k][l] == 0 and used[k][l] == 0:
            ret = bfs(k,l)
            chance +=1
            result.append(ret)

result.sort()
print(chance)
print(*result)
