#2차원 배열의 합
#문제에서 x부터 제시했고 순서대로 돌아가는 문제이므로 x축부터 돌려야함
def hop(sx,sy,ex,ey):
    hop = 0
    for a in range(sx-1,ex):
            for b in range(sy-1,ey):
                hop += arr[a][b]

    return hop


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    result = 0
    i,j,x,y = map(int,input().split())
    result += hop(i,j,x,y)
    print(result)

