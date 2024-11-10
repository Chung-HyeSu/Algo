from collections import deque
def bfs(maps):
    q = deque()
    q.append([0,0,1])
    
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    
    while q:
        y,x,cnt = q.popleft()
        
        if y==n-1 and x==m-1:
            return cnt
        
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x

            if 0<=dy<n and 0<=dx<m and maps[dy][dx] == 1 and visited[dy][dx] == False: #1은 길, 0은 벽
                visited[dy][dx] = True
                q.append([dy,dx,cnt+1])
                
    return -1
        
    
    
def solution(maps):
    global n,m
    
    n = len(maps) #세로
    m = len(maps[0]) #가로
    
    return bfs(maps)