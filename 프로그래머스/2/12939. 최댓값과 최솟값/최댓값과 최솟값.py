def solution(s):
    
    lst = list(map(int,s.split()))
    mini = min(lst)
    maxi = max(lst)

    return f'{mini} {maxi}'