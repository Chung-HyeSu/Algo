#더하거나 빼서 타겟넘버
#numbers: 숫자배열, target: 목표

def dfs(numbers,target,depth,cur):
    global answer
    if depth == len(numbers):
        if cur == target:
            answer += 1
        return
    
    #더하는 경우
    dfs(numbers, target, depth+1, cur+numbers[depth])
    
    #빼는 경우
    dfs(numbers, target, depth+1, cur-numbers[depth])
    

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0,0)
    return answer
