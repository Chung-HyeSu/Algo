def solution(num_list):

    if num_list[-1] > num_list[-2] :
        target = num_list[-1]-num_list[-2]
        num_list.append(target)
        return num_list
    elif num_list[-1] <= num_list[-2] :
        num_list.append(num_list[-1]*2)
        return num_list