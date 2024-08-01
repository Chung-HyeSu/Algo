#14888
N = int(input())
A_lst = list(map(int,input().split()))
B_lst = list(map(int,input().split())) # + - * /


#백트래킹 문제
#재귀를 이용하는 것이 가장 좋을 것
max_value = -21e8
min_value = 21e8

def dfs(total, level, plus, minus, gop, nanugi):
    global max_value, min_value
    if level == N:
        max_value = max(total, max_value)
        min_value = min(total, min_value)
        return

    if plus:
        dfs(total+A_lst[level], level+1, plus-1, minus, gop, nanugi)
    if minus:
        dfs(total-A_lst[level], level+1, plus, minus-1, gop, nanugi)
    if gop:
        dfs(total*A_lst[level], level+1, plus, minus, gop-1, nanugi)
    if nanugi:
        if total < 0:
            dfs((total*(-1)//A_lst[level])*(-1), level+1, plus, minus, gop, nanugi-1)
        else:
            dfs(total//A_lst[level], level+1, plus, minus, gop, nanugi-1)

dfs(A_lst[0],1,B_lst[0], B_lst[1], B_lst[2], B_lst[3])
print(max_value)
print(min_value)