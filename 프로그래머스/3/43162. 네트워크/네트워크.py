def dfs(n, computers, now):
    global answer, visited
    
    visited[now] = True
    for i in range(n):
        if i != now and computers[now][i] == 1 and visited[i] == False:
            dfs(n, computers, i)

def solution(n, computers):
    global answer, visited
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i)
            answer += 1
    
    return answer