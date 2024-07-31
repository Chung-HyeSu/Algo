from collections import deque
N, K = map(int,input().split())#수빈, 동생

def cal(N,K):
    q = deque()
    q.append(N)

    max_limit = 100001
    visited = [0]*max_limit
    ways = [0]*max_limit
    visited[N] = 1
    ways[N]= 1

    while q:
        cur = q.popleft()
        for next_cur in (cur-1, cur+1, cur*2):
            if 0<= next_cur < max_limit:
                if not visited[next_cur]:
                    visited[next_cur] = visited[cur]+1
                    ways[next_cur] = ways[cur]
                    q.append(next_cur)
                elif visited[next_cur] == visited[cur]+1:
                    ways[next_cur] += ways[cur]
    return visited[K]-1, ways[K]



time,way = cal(N,K)
print(time)
print(way)