from collections import deque
R,C = map(int,input().split()) #세로, 가로
arr = [list(input()) for _ in range(R)]
num_v = 0
num_k = 0

def bfs(y,x):
    global num_v,num_k
    q = deque()
    q.append([y,x])
    here_v = 0 #늑대
    here_k = 0 #양
    if arr[y][x] == 'v':
        here_v += 1
    elif arr[y][x] == 'k':
        here_k += 1
    arr[y][x] = 'x'

    while q:
        qy,qx = q.popleft()
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + qy
            dx = directx[i] + qx
            if dy<0 or dy>=R or dx<0 or dx>=C : continue
            if arr[dy][dx] == '#' : continue
            if arr[dy][dx] == '.' :
                q.append([dy,dx])
                arr[dy][dx] = 'x'
            elif arr[dy][dx] == 'v' :
                q.append([dy,dx])
                here_v += 1
                arr[dy][dx] = 'x'
            elif arr[dy][dx] == 'k':
                q.append([dy,dx])
                here_k += 1
                arr[dy][dx] = 'x'


    if here_k>here_v:
        num_k += here_k
        # print('양', here_k)

    else:
        num_v += here_v
        # print('늑',here_v)



for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v' or arr[i][j] == 'k':
            bfs(i,j)

print(num_k,num_v)