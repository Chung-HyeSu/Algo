def solution(n):
    answer = 0
    
    for i in range(n+1):
        # n이 홀 수 일때
        if n%2 == 1 and i%2 == 1:
            answer += i
        # n이 짝 수 일때
        elif n%2 == 0 and i%2 == 0:
            answer += i*i
            
    
    
    return answer
