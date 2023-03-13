#적록색약
import sys
sys.setrecursionlimit(100000)
N = int(input())
arr = [list(input()) for _ in range(N)]

used = [[0]*N for _ in range(N)]

def normal(y,x):
    target_normal = arr[y][x]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    for i in range(4):
        dy = directy[i]+y
        dx = directx[i]+x
        if dy<0 or dx<0 or dy>=N or dx>=N : continue
        if used[dy][dx] == 1 : continue
        if arr[dy][dx] == target_normal:
            used[dy][dx] = 1
            normal(dy,dx)


cnt_normal = 0
cnt = 0

for i in range(N):
    for j in range(N):
        if used[i][j] == 0:
            normal(i,j)
            cnt_normal += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

used = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if used[i][j] == 0:
            normal(i,j)
            cnt += 1



print(cnt_normal, cnt)