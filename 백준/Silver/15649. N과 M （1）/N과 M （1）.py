import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False]*n
ans = []



def dfs(depth):
    if depth == m:
        print(*ans)
        return

    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            dfs(depth+1)
            ans.pop()

dfs(0)