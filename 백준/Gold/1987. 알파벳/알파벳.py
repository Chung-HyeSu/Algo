#알파벳
import sys
sys.setrecursionlimit(100000)

def dfs(y,x,cnt):
    global path, Max
    if cnt > Max:
        Max = cnt

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy<0 or dx<0 or dy>=R or dx>=C: continue
        if arr[dy][dx] not in path:
            path.add(arr[dy][dx])
            dfs(dy,dx,cnt+1)
            path.remove(arr[dy][dx])





R,C = map(int,input().split())
arr= [list(input()) for _ in range(R)]
used = [[0]*C for _ in range(R)]
Max = -21e8
path = set()
path.add(arr[0][0])
dfs(0,0,1)
print(Max)

#path.add(), path.remove