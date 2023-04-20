#농장 관리
def dfs(ty,tx):
    global trigger
    visited[ty][tx] = True

    for i in range(8):
        dy = ty+directy[i]
        dx = tx+directx[i]
        if dy<0 or dx<0 or dy>=N or dx>=M : continue
        if arr[dy][dx] > arr[ty][tx]:
            trigger = False
        if not visited[dy][dx] and arr[dy][dx] == arr[ty][tx]:
            dfs(dy,dx)

N, M = map(int,input().split()) #세로, 가로
arr = [list(map(int,input().split())) for _ in range(N)]
directy = [-1,-1,-1,0,0,1,1,1]
directx = [-1,0,1,-1,1,-1,0,1]

result = 0
visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] >0 and not visited[i][j]:
            trigger = True
            dfs(i,j)

            if trigger:
                result+=1

print(result)