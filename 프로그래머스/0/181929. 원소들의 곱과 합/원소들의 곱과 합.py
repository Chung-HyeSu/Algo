def solution(num_list):
    gob = 1
    hop = 0
    
    for i in range(len(num_list)):
        gob = gob*num_list[i]
        hop = hop+num_list[i]
        
    return 1 if gob < hop**2 else 0