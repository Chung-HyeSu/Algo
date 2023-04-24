# 유기농 배추
from collections import deque
def bfs(i,j):
    q = deque()
    q.append([i,j])

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        now = q.popleft()
        y,x = now[0],now[1]

        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy<0 or dx<0 or dy>=N or dx>=M : continue
            if arr[dy][dx] == 1 :
                q.append([dy,dx])
                arr[dy][dx] = 0

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split()) #가로, 세로, 개수
    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        a,b = map(int,input().split())
        arr[b][a] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 :
                bfs(i,j)
                result += 1

    print(result)