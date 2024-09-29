import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #1~n까지 중 m개를 고른 수열. 같은 수를 여러번 골라도 됨. 수열이 중복되면 안됨

ans = []


def back():
    if len(ans) == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(i+1)
        back()
        ans.pop()

back()