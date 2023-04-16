from collections import deque

def bfs(i, j):
    global visited
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        now = q.popleft()
        y, x = now[0], now[1]

        for i in range(8):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dy >= h or dx >= w: continue
            if arr[dy][dx] == 0 or visited[dy][dx] == 1: continue
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                q.append([dy, dx])
                visited[dy][dx] = 1

while True:
    w,h = map(int,input().split()) #가로, 세로
    if w == 0 and h == 0:
        break
    else:
        arr = [list(map(int,input().split())) for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        directy = [-1,-1,-1,0,0,1,1,1] #왼쪽위부터 123, 4,6,789
        directx = [-1,0,1,-1,1,-1,0,1]

        result = 0
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1 and visited[i][j] == 0:
                    bfs(i,j)
                    result += 1

        print(result)