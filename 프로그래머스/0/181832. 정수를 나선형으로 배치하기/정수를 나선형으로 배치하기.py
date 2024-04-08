# 달팽이
def solution(n):
    arr = [[0]*n for _ in range(n)]
    # arr = [[0]*n]*n

    dy = [0,1,0,-1] #우하좌상
    dx = [1,0,-1,0]

    y,x = 0,0
    direction = 0


    for i in range(1,n*n+1):
        arr[y][x] = i
        y += dy[direction]
        x += dx[direction]
        if y<0 or y>=n or x<0 or x>=n or arr[y][x] != 0:
            y -= dy[direction]
            x -= dx[direction]
            direction = (direction+1)%4
            y += dy[direction]
            x += dx[direction]

    return arr

