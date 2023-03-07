#DFS와 BFS
from collections import deque

def dfs(level):
    used[level] = 1
    print(level,end=' ')

    for i in range(1,N+1):
        if arr[level][i] == 1 and used[i] == 0:
            dfs(i)


N, M, V = map(int,input().split()) #정점, 간선, 탐색시작할 번호
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1

used = [0]*(N+1)
used2 = [0]*(N+1)


def bfs(v):
    q = deque()
    q.append(v)
    used2[v] = 1

    while q:
        now = q.popleft()
        print(now,end=' ')

        for i in range(1, N+1):
            if arr[now][i] == 1 and used2[i] == 0:
                q.append(i)
                used2[i] = 1





dfs(V)
print()
bfs(V)