#보물섬
from collections import deque
def bfs(i,j):
     q = deque()
     q.append([i,j,0])
     used = [[0]*W for _ in range(L)]
     used[i][j] = 1
     result = -21e8

     while q:
         now = q.popleft()
         y,x,cnt = now[0],now[1],now[2]
         if cnt>result:
             result = cnt

         directy = [-1,1,0,0]
         directx = [0,0,-1,1]
         for i in range(4):
             dy = directy[i] + y
             dx = directx[i] + x
             if dy<0 or dx<0 or dy>=L or dx>=W : continue
             if arr[dy][dx] == 'L' and used[dy][dx] == 0:
                 q.append([dy,dx,cnt+1])
                 used[dy][dx] = 1
     return result



L,W = map(int,input().split()) #세로, 가로
arr = [list(input()) for _ in range(L)]

Max = -21e8
for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L' :
            ret = bfs(i,j)
            Max = max(ret,Max)

print(Max)