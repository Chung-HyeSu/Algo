def solution(a, d, included):
    answer = 0
    sum_seq= 0

    for i in range(len(included)):
        sum_seq = a+d*i
        if included[i] == True:
            answer += sum_seq

    return answer
