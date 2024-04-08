def solution(arr, queries):
    for i in range(len(queries)):
        a,b = queries[i][0], queries[i][1]
        A = arr[a]
        B = arr[b]
        arr[a] = B
        arr[b] = A
    
    return arr