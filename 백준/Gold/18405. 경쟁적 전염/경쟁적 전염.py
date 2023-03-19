#경쟁적 전염
from collections import deque
N, K = map(int,input().split()) #NxN 크기의 맵. K번까지의 바이러스
arr= [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split()) #S초 뒤 X,Y 좌표 값을 출력

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append([arr[i][j], i, j])
virus.sort()


def bfs(S,X,Y):
    q = deque(virus)
    time = 0

    while q:
        if time == S:
            break

        for _ in range(len(q)):
            now = q.popleft()
            v,y,x = now[0],now[1],now[2]

            directy = [-1,1,0,0]
            directx = [0,0,-1,1]
            for i in range(4):
                dy = y+directy[i]
                dx = x+directx[i]
                if dy<0 or dx<0 or dy>=N or dx>=N : continue
                if arr[dy][dx] != 0: continue
                arr[dy][dx] = arr[y][x]
                q.append([arr[dy][dx],dy,dx])
        time += 1
    return arr[X-1][Y-1]


print(bfs(S,X,Y))

