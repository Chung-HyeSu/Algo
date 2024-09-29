#6987

#각 조별 6개국. 각 국가별 총 5번 경기. => 총 15경기
#결과가 가능한지.

import sys
input = sys.stdin.readline

#가능한 경우의 수 조합 == 두 팀의 경기
from itertools import combinations as cb
result = list(cb(range(6),2)) #[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]


def dfs(depth):
    global cnt
    if depth == 15:
        cnt = 1
        for g in game:
            if g.count(0) != 3:
                cnt = 0
                break
        return

    t1,t2 = result[depth] #(0,1)이면 t1이 A, t2가 B
    #승무패 비교
    for r_t1,r_t2 in ((0,2), (1,1), (2,0)):
        if game[t1][r_t1] > 0 and game[t2][r_t2] >0 :
            game[t1][r_t1] -=1
            game[t2][r_t2] -=1
            dfs(depth+1)
            game[t1][r_t1] += 1
            game[t2][r_t2] += 1




ans = []
for _ in range(4):
    all_games = list(map(int,input().split()))
    game = [all_games[i:i+3] for i in range(0,18,3)]
    cnt = 0
    dfs(0)
    ans.append(cnt)

print(*ans)

#[[5, 0, 0], [4, 0, 1], [2, 2, 1], [2, 0, 3], [1, 0, 4], [0, 0, 5]]