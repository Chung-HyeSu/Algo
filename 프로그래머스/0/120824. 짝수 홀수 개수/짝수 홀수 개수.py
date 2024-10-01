def solution(num_list):
    zzac = 0
    hol = 0
    
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            zzac += 1
        else : 
            hol += 1
    answer = [zzac, hol]
            
    
    return answer