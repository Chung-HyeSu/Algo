from collections import deque
def bfs(maps):
    q = deque()
    q.append([0,0,1])
    
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    ty = n-1
    tx = m-1

    while q:
        y,x,cnt = q.popleft()
        if y == ty and x == tx:
            return cnt
        
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i]+ y
            dx = directx[i]+ x
            if 0<=dy<n and 0<=dx<m and maps[dy][dx] == 1 and visited[dy][dx] == False:
                visited[dy][dx] = True
                q.append([dy,dx,cnt+1])

    return -1
                
        

def solution(maps):
    global n,m
    
    answer = 0
    
    n = len(maps) #행
    m = len(maps[0]) #열
    
    return bfs(maps)
    

    
    
