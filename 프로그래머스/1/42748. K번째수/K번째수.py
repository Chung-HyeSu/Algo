def solution(array, commands):
    answer = []
    
    for i,com in enumerate(commands):
        target = sorted(array[com[0]-1:com[1]])
        answer.append(target[com[2]-1])
    
    
        
    
    
    return answer