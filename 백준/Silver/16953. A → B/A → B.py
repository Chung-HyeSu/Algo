from collections import deque
A, B = map(int,input().split())
def b_calcul(A,B):
    q = deque()
    q.append([A,1])
    while q:
        cur, cnt = q.popleft()

        if cur == B:
            return cnt

        if cur*2 <= B:
            q.append([cur*2,cnt+1])

        if int(str(cur)+'1') <= B:
            q.append([int(str(cur)+'1'),cnt+1])
    return -1

print(b_calcul(A,B))