#공주님을 다시 구해라
from collections import deque
N,M,T = map(int,input().split()) #세로, 가로, 제한시간
arr = [list(map(int,input().split())) for _ in range(N)]

used = [[0]*M for _ in range(N)]

directy = [-1,1,0,0]
directx = [0,0,-1,1]

def bfs():
    ret = 21e8
    q = deque()
    q.append([0,0])
    used[0][0] = 0

    while q:
        now = q.popleft()
        y,x = now[0],now[1]

        for i in range(4):
            dy = directy[i]+y
            dx = directx[i]+x

            if dy == N-1 and dx == M-1 :
                return min(used[y][x]+1, ret)

            if dy<0 or dx<0 or dy>=N or dx>=M : continue
            if used[dy][dx] != 0: continue
            if arr[dy][dx] == 0:
                used[dy][dx] = used[y][x] + 1
                q.append([dy,dx])
            elif arr[dy][dx] == 2:
                used[dy][dx] = used[y][x] + 1
                ret = min(ret,used[dy][dx]+abs(N-1-dy)+abs(M-1-dx))
    return ret

ans = bfs()

print('Fail' if ans > T else ans)