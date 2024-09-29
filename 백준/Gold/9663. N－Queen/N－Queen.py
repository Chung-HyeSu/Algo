#대각선은 행차이 == 열차이 같다는 점★

def attack(x):
    #x는 현재 퀸이 놓인 자리 -> row[x] : 현재 퀸이 놓인 행, x: 현재 퀸이 놓인 열
    #i는 이제 놓일 자리 -> row[i] : 이제 퀸이 놓일 행, i: 이제 퀸이 놓일 열
    for i in range(x):
        #공격을 받는 경우
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return True
    return False


def dfs(queen):
    global cnt
    if queen == n:
        cnt += 1
        return

    for i in range(n):
        row[queen] = i
        if not attack(queen):
            dfs(queen+1)




n = int(input())
row = [0]*n
cnt = 0
dfs(0)
print(cnt)