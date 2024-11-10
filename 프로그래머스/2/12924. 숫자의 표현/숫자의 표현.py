def solution(n):
    global answer
    answer = 0
    
    def go(st):
        global answer
        if st == n:
            answer += 1
            return 
        
        hop = 0
        for i in range(st, n+1):
            hop += i
            if hop > n:
                break
            elif hop < n:
                continue
            elif hop == n:
                print(st,'hihi')
                answer += 1
                break
    
    for i in range(1,n+1):
        go(i)
    
    return answer