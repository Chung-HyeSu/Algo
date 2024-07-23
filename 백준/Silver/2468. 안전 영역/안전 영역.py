#2468 안전영역
#장마철에 물에 잠기지 않는 안전영역의 최대 개수 구하기
#높이는 1~100
import copy
from collections import deque
N = int(input()) #맵 영역
arr = [list(map(int,input().split())) for _ in range(N)]
directy = [-1,1,0,0]
directx = [0,0,-1,1]
cnt = 0
Max = -21e8

def bfs(rain,y,x):
    q = deque()
    q.append([y,x])

    while q:
        nowy,nowx = q.popleft()
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy<0 or dy>=N or dx<0 or dx>=N: continue
            if arr[dy][dx]<=rain: continue
            q.append([dy,dx])
            arr[dy][dx] = 0


backup = copy.deepcopy(arr)
for r in range(100):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > r:
                bfs(r,i,j)
                cnt+=1
    Max = max(cnt,Max)
    arr = copy.deepcopy(backup)

print(Max)