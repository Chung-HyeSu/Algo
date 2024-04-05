def solution(a, b):
    A = int(f'{a}{b}')
    B = int(f'{2*a*b}')
    if A == B:
        return A
    else:
        return max(A, B)