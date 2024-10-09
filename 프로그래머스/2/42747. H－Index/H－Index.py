def solution(citations):
    answer = 0

    for target in range(1,len(citations)+1):
        quoted = 0
        for j in range(len(citations)):
            if target <= citations[j]:
                quoted += 1
        print(target, quoted)
        if target <= quoted:
            answer = target

    
    return answer