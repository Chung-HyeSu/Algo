import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = [0]



def dfs(depth):
    if depth == m:
        print(*ans[1:])
        return

    prev = ans[-1]
    for i in range(1,n+1):
        if i>= prev:
            ans.append(i)
            dfs(depth+1)
            ans.pop()




dfs(0)