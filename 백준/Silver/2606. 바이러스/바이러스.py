#2606 바이러스
N = int(input()) #컴퓨터 수
M = int(input()) #컴퓨터 쌍 수

arr = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
visited_list = [1]

for i in range(M):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


def abc(cpu):

    for i in range(N):
        if arr[cpu][i] == 1 and visited[cpu][i] == False:
            visited[cpu][i] = True
            if i+1 not in visited_list:
                visited_list.append(i+1)
            abc(i)

visited[0][0] = True
abc(0)
print(len(visited_list)-1)