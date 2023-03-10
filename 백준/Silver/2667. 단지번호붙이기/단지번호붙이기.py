#단지번호 붙이기
from collections import deque
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    cnt = 1
    used = [[0]*N for _ in range(N)]
    used[y][x] = 1
    arr[y][x] = town

    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if 0<=dy<N and 0<=dx<N and arr[dy][dx] == 1 and used[dy][dx] == 0:
                cnt+=1
                used[dy][dx] = 1
                arr[dy][dx] = town
                q.append([dy,dx])
    return cnt

town = 100
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            town +=1
            ret = bfs(i,j)
            house.append(ret)

print(town-100)
house.sort()
for i in range(len(house)):
    print(house[i])
