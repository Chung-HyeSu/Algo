#2644 촌수계산
n = int(input())
t1,t2 = map(int,input().split())
m = int(input())

arr = [[0]*n for _ in range(n)]
visited = [False]*n
for _ in range(m):
    p,c = map(int,input().split())
    arr[p-1][c-1] = 1
    arr[c-1][p-1] = 1


def abc(current,target,distance):
    if current == target:
        return distance

    visited[current] = True

    for i in range(n):
        if arr[current][i] == 1 and not visited[i]:
            result = abc(i,target,distance+1)
            if result != -1:
                return result
    return -1


print(abc(t1-1,t2-1,0))