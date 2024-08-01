#2504
arr = list(input())

# 여는 괄호는 스택에 넣고, 닫는 괄호는 스택에서 꺼내 짝을 비교

def cal():
    stack = []
    cur_value = 1
    res_value = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
            cur_value *= 2
        elif arr[i] == '[':
            stack.append(arr[i])
            cur_value *= 3
        elif arr[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if arr[i-1] == '(':
                res_value += cur_value
            stack.pop()
            cur_value //= 2
        elif arr[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if arr[i-1] == '[':
                res_value += cur_value
            stack.pop()
            cur_value //= 3

    if stack:
        return 0
    return res_value




print(cal())