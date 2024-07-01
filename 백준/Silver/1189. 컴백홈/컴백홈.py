R,C,K = map(int,input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

directy = [-1,1,0,0] #상하좌우
directx = [0,0,-1,1]

cnt = 0
def abc(level,y,x):
    global cnt
    if level > K:
        return
    if level == K and y == 0 and x == C-1:
        cnt += 1
        return

    for i in range(4):
        dy = y+directy[i]
        dx = x+directx[i]
        if 0<=dy<R and 0<=dx<C and arr[dy][dx] == '.':
            arr[dy][dx] = 'T'
            abc(level+1,dy,dx)
            arr[dy][dx] = '.'


arr[R-1][0] = 'T'
abc(1,R-1,0)
print(cnt)