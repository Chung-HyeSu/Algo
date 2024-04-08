def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        target = numLog[i]-numLog[i-1]
        if target == 1:
            answer += 'w'
        elif target == -1 :
            answer += 's'
        elif target == 10:
            answer += 'd'
        elif target == -10:
            answer += 'a'

    return answer