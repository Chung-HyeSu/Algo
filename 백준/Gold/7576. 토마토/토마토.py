#토마토
from collections import deque
def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append([i,j,1])

    while q:
        now = q.popleft()
        y,x,cnt = now[0],now[1],now[2]
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if 0<=dy<N and 0<=dx<M and arr[dy][dx] == 0:
                q.append([dy,dx,cnt+1])
                arr[dy][dx] = cnt


M,N = map(int,input().split()) #가로, 세로
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))



flag = 1
for i in range(N):
    if flag:
        for j in range(M):
            #모두 익은 상태일때
            if arr[i][j] != 0:
                continue
            #익을 토마토가 있는 상태
            elif arr[i][j] == 0:
                flag = 0
                break

if flag :
    print(0)
else:
    bfs()
    Max = -21e8
    flag2 = 1
    for i in range(N):
        if flag2 :
            for j in range(M):
                if arr[i][j] == 0:
                    flag2 = 0
                    break
                elif arr[i][j] > Max:
                    Max = arr[i][j]
    print(Max if flag2 else -1)



