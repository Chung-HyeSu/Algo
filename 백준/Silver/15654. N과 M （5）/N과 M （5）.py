n,m = map(int,input().split())
lst = sorted(list(map(int,input().split()))) #n개의 수
ans = []

#중복X lst 중에서 m개 고른것
def dfs(cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(n):
        if lst[i] not in ans:
            ans.append(lst[i])
            dfs(cnt+1)
            ans.pop()


dfs(0)