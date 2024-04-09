def solution(arr, queries):
    answer = []
    for i in queries:
        s,e,k = i[0],i[1],i[2]
        target = 1000000
        for j in range(len(arr)):
            if s<=j<=e and arr[j]>k :
                target = min(target, arr[j])
        if target != 1000000:
            answer.append(target)
        else:
            answer.append(-1)
    return answer