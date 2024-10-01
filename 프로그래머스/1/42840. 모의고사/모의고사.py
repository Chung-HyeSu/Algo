def solution(answers):
    answer = []
    n = len(answers)
    
    def no1(n):
        score_1 = 0
        lst_1 = [1,2,3,4,5]
        
        for i in range(n):
            if lst_1[i%len(lst_1)] == answers[i]:
                score_1 += 1
        
        return score_1
    
    def no2(n):
        score_2 = 0
        lst_2 = [2,1,2,3,2,4,2,5]
        
        for i in range(n):
            if lst_2[i%len(lst_2)] == answers[i]:
                score_2 += 1
        return score_2
    
    def no3(n):
        score_3 = 0
        lst_3 = [3,3,1,1,2,2,4,4,5,5]
        
        for i in range(n):
            if lst_3[i%len(lst_3)] == answers[i]:
                score_3 += 1
        return score_3
    
    
    score = [no1(n), no2(n), no3(n)]
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
    
    answer = sorted(answer)
            
    
    return answer