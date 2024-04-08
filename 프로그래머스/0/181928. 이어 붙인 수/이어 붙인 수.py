def solution(num_list):
    hol = ''
    zzac = ''

    for i in range(len(num_list)):
        if num_list[i]%2 == 0 :
            zzac += str(num_list[i])
        else :
            hol += str(num_list[i])
            
    return int(hol)+int(zzac)