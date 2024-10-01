def solution(brown, yellow):
    answer = []
    
    # brown + yellow = 2*g+2*s+4+gs
    # yellow = g*s
    # brown = 2*g+2*s+4
    
    for s in range(brown):
        for g in range(s,brown):
            if yellow == g*s and brown == 2*g+2*s+4:
                answer.append(g+2)
                answer.append(s+2)
    
    # print(answer)

    
    return answer