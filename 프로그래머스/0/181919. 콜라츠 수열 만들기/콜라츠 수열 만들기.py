def solution(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n%2 == 0:
            N = n/2
            answer.append(N)
            n = N
        elif n%2 == 1:
            N = 3*n+1
            answer.append(N)
            n = N
    return answer