def solution(word):
    answer = []
    mouem = ['A','E','I','O','U']
    
    def make_words(cur,length):
        if length == 0:
            answer.append(cur)
            return 
        
        for mo in mouem:
            make_words(cur+mo, length-1)
    
    
    for length in range(1,6):
        make_words('',length)
    
    answer.sort()
    
    
    return answer.index(word)+1