import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False]*n
ans = [0]



def dfs(depth,idx):
    if depth == m:
        print(*ans[1:])
        return

    prev_num = ans[-1]
    for i in range(idx,n+1):
        if i not in ans and i>prev_num:
            ans.append(i)
            dfs(depth+1, idx+1)
            ans.pop()




dfs(0,1)