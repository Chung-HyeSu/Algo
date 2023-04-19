#음식물 피하기
from collections import deque
def bfs(y,x):
    q = deque()
    q.append([y,x])
    trash = 0

    while q:
        now = q.popleft()
        y,x = now[0], now[1]
        for i in range(4):
            dy = y+ directy[i]
            dx = x+ directx[i]
            if dy<0 or dx<0 or dy>=N or dx>=M : continue
            if arr[dy][dx] == 0: continue
            if arr[dy][dx] == 1:
                trash += 1
                q.append([dy,dx])
                arr[dy][dx] = 0
    return trash



N, M, K = map(int,input().split()) #세로, 가로, 음식물쓰레기 개수
arr = [[0]*M for _ in range(N)]
directy = [-1,1,0,0]
directx = [0,0,-1,1]

for k in range(K):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ret = bfs(i,j)
            result = max(ret, result)

print(result)
