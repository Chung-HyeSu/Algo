#3460
T = int(input())
for _ in range(T):
    n = int(input())
    ans = ''

    # 8 4 2 1
    # 13이면 1 1 0 1

    while n>0:
        ans += str(n%2)
        n = n//2

    for i in range(len(ans)):
        if ans[i] == '1':
            print(i, end=' ')