def solution(arr):
    answer = []
    prev = -1
    for sub in arr:
        if sub != prev : 
            answer.append(sub)
            prev = sub
    
    return answer