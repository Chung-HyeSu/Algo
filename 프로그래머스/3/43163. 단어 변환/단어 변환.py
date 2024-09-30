from collections import deque

def solve(begin, target, words):
    q = deque()
    q.append([begin,0])
    
    visited = [False]*len(words)

    
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        
        for idx, word in enumerate(words):
            dif = 0
            for i in range(len(now)):
                if word[i] != now[i] and not visited[idx]:
                    dif += 1
            if dif == 1: #같은게 2개일 때만 바꿀 수 있음. 
                q.append([word,cnt+1])
                visited[idx] = True
    return 0
                
                    

def solution(begin, target, words):
    
    if target not in words:
        return 0
    else:
        return solve(begin, target, words)
    
    