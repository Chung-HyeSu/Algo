from collections import deque
R,C = map(int,input().split()) #행, 열
arr = [list(map(str,input())) for _ in range(R)]
sheep = 0
wolf = 0

def bfs(y,x):
    global sheep, wolf
    q = deque()
    q.append([y,x])
    sheep_tem = 0
    wolf_tem = 0
    if arr[y][x] == 'o' :
        sheep_tem += 1
        arr[y][x] = 0
    elif arr[y][x] == 'v' :
        wolf_tem += 1
        arr[y][x] = 0

    while q:
        y,x = q.popleft()
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy<0 or dy>=R or dx<0 or dx>=C : continue
            if arr[dy][dx] == '#' or 0 : continue
            if arr[dy][dx] == '.' :
                q.append([dy,dx])
                arr[dy][dx] = 0
            elif arr[dy][dx] == 'o':
                sheep_tem += 1
                q.append([dy,dx])
                arr[dy][dx] = 0
            elif arr[dy][dx] =='v':
                wolf_tem += 1
                q.append([dy,dx])
                arr[dy][dx] = 0
    if sheep_tem>wolf_tem:
        # print(sheep_tem,'sheep')
        sheep += sheep_tem
    else:
        # print(wolf_tem,'wolf')
        wolf += wolf_tem




for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v' or arr[i][j] == 'o':
            bfs(i,j)


print(sheep, wolf)