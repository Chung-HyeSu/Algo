A, B = map(int,input().split())

def calcul(A,B):
    cnt = 0
    while B>A:
        if B%2 == 0:
            B = B//2
        elif B%10 == 1:
            B = B//10
        else:
            break
        cnt += 1

    if A == B:
        return cnt+1
    else: 
        return -1

print(calcul(A,B))