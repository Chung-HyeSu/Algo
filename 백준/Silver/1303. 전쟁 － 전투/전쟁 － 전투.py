from collections import deque
N,M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(M)]
W_power = 0
B_power = 0


def bfs(y,x,team):
    global W_power, B_power
    q = deque()
    q.append([y,x])
    arr[y][x] = 0
    power = 1

    while q:
        nowy,nowx = q.popleft()
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy<0 or dy>=M or dx<0 or dx>=N : continue
            if arr[dy][dx] == 0 or arr[dy][dx] != team: continue
            if arr[dy][dx] == team :
                power += 1
                q.append([dy,dx])
                arr[dy][dx] = 0

    if team == 'W':
        W_power += power*power
    elif team == 'B':
        B_power += power*power


for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W' or 'B':
            bfs(i,j,arr[i][j])

print(W_power,B_power)