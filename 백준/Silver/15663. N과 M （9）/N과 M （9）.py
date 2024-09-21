N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False]*N
temp = []
#사전순으로 증가하는 순으로 수열 출력하기, 중복되는건 제외

def back():
    global M
    if len(temp) == M:
        print(*temp)
        return

    temp_num = 0
    for i in range(N):
        if not visited[i] and temp_num != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            temp_num = nums[i]
            back()
            visited[i] = False
            temp.pop()



back()
