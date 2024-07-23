from collections import deque
arr = [list(map(int,input().split())) for _ in range(5)]
ans_list = []

directy = [-1,1,0,0]
directx = [0,0,-1,1]

def dfs(y,x,level,ans_num):
    ans_num += str(arr[y][x])
    if level == 5:
        if ans_num not in ans_list :
            ans_list.append(ans_num)
        return

    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy<0 or dy>=5 or dx<0 or dx>=5:continue
        dfs(dy,dx,level+1,ans_num)




for i in range(5):
    for j in range(5):
        dfs(i,j,0,str(arr[i][j]))

print(len(ans_list))