
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

visited = [False]*n
temp = []

def back():
    if len(temp) == m:
        print(*temp)
        return

    temp_num = 0
    for i in range(n):
        if not visited[i] and temp_num != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            temp_num = nums[i]
            back()
            visited[i] = False
            temp.pop()


back()