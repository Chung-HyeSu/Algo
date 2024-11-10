def dfs(numbers, target, depth, cur):
    global answer
    if depth == len(numbers):
        if cur == target:
            answer += 1
        return 

    dfs(numbers, target, depth+1, cur+numbers[depth])

    dfs(numbers, target, depth+1, cur-numbers[depth])
    
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer