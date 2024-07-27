from collections import deque
M,N = map(int,input().split()) #세로, 가로
arr = [list(map(int,input().split())) for _ in range(M)]
cnt = 0

def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        nowy,nowx = q.popleft()
        arr[nowy][nowx] = 0
        directy = [-1,-1,-1,0,0,1,1,1] #왼쪽위부터 123,456,789
        directx = [-1,0,1,-1,1,-1,0,1]
        for i in range(8):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy<0 or dy>=M or dx<0 or dx>=N : continue
            if arr[dy][dx] == 1:
                q.append([dy,dx])
                arr[dy][dx] = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i,j)
            cnt += 1

print(cnt)