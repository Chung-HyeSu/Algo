def solution(begin, target, words):
    global answer
    visited = [False]*len(words)
    answer = 21e8
    
    def is_same(cur,word):
        dif = 0
        for i in range(len(word)):
            if cur[i] != word[i]:
                dif += 1
        return dif
        
    
    def dfs(cur, cnt):
        global answer
        if cur == target:
            answer = min(answer, cnt)
            return
        
        for i,word in enumerate(words):
            if is_same(cur,word) == 1 and not visited[i]:
                visited[i] = True
                dfs(word, cnt+1)
                visited[i] = False
                
                
    if target not in words:
        return 0
    else:
        dfs(begin,0)
        
        if answer == 21e8:
            return 0
        else:
            return answer