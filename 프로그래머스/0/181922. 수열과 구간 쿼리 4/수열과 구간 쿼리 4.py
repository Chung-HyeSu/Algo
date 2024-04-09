def solution(arr, queries):
    for i in queries:
        s,e,k = i[0],i[1],i[2]
        for j in range(len(arr)):
            if s<=j<=e and j%k == 0:
                arr[j] += 1
    return arr