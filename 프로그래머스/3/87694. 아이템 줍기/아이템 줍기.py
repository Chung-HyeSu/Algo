def solution(rectangle, characterX, characterY, itemX, itemY):
    global way
    answer = 0
    way = 21e8
    
    maps = [[0]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    
    def marking(x1,y1,x2,y2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if x == x1 or x == x2 or y == y1 or y == y2:
                    if maps[y][x] != 2:
                        maps[y][x] = 1
                else:
                    maps[y][x] = 2
                    
    
    def explore(x,y,fx,fy,cnt):
        global way
        if x == fx and y == fy:
            way = min(way, cnt)
            return 
        
        visited[y][x] = True
        
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0<=dy<102 and 0<=dx<102:
                if maps[dy][dx] == 1 and visited[dy][dx] == False:
                    visited[dy][dx] = True
                    explore(dx,dy,fx,fy,cnt+1)
                    visited[dy][dx] = False
        
    
    
    
    for rec in rectangle:
        marking(2*rec[0], 2*rec[1], 2*rec[2], 2*rec[3])
        
    explore(2*characterX, 2*characterY, 2*itemX, 2*itemY, 1)
    
    
    return way//2