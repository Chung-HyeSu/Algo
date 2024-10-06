def solution(priorities, location):
    answer = 0
    n = len(priorities)
    visited = [False]*n
    seq_lst = [0]*n
    seq = 1

    
    while visited.count(False) > 0:
        
        for i in range(n):
            if not visited[i]:
                pri = max(priorities)
                if priorities[i] == pri:
                    visited[i] = True
                    seq_lst[i] = seq
                    priorities[i] = -1
                    seq += 1
        pri = -21e8
        
    
    
    return seq_lst[location]