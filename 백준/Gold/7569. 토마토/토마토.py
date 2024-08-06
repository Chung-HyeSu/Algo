#tomato
#3차원 문제. 상하좌우 평면과 높이를 따로 분리해서 풀이
#BFS
from collections import deque
M,N,H = map(int,input().split()) #가로, 세로, 높이
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
direct = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]#y,x,h 순서. 상 하 좌 우 +1층 -1층

def Tomato(st_tomato):
    q = deque(st_tomato)
    day = 0

    while q:
        h,y,x,d = q.popleft()
        day = d

        for dh,dy,dx in direct:
            nh,ny,nx = h+dh, y+dy,x+dx
            if 0<=nh<H and 0<=ny<N and 0<=nx<M and arr[nh][ny][nx] == 0:
                arr[nh][ny][nx] = 1 #익었다고 표기
                q.append([nh,ny,nx,d+1])

    #박스 내부에 토마토가 모두 익었는지 체크
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return -1 #전부 안익은 경우는 여기서 체크
    return day

#01. 익은 토마토 찾기. 1: 익은 토마토, 0: 안익은 토마토, -1: 빈칸
st_tomato = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                st_tomato.append([h,i,j,0])

#02. 먼저 익은 토마토 갯수에 따라 익은 토마토가 없으면 -1, 전부 익은 토마토면 0 출력
if len(st_tomato) == M*N*H:
    print(0)
else:
    result = Tomato(st_tomato)
    print(result)

