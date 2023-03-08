#미로탐색 - BFS
from collections import deque
N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)] #1로 이동가능 #0,0출발 -> N,M 도착

def bfs(sy,sx):
    q = deque()
    q.append([sy,sx,1])
    used = [[0]*M for _ in range(N)]
    used[sy][sx] = 1
    Min = 21e8
    while q:
        now = q.popleft()
        y,x,cnt = now[0],now[1],now[2]
        if y == N-1 and x == M-1:
            if cnt<Min:
                Min = cnt
        directy = [-1,1,0,0] #상하좌우
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if 0<=dy<N and 0<=dx<M and arr[dy][dx] == 1 and used[dy][dx] == 0 :
                q.append([dy,dx,cnt+1])
                used[dy][dx] = 1
    return Min

print(bfs(0,0))
