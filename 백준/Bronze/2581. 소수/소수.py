#2581
M = int(input())
N = int(input())
ans = []
for i in range(M,N+1):
    cur = 0
    for j in range(1,i+1):
        if i%j == 0:
            cur +=1
    if cur == 2:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else :
    print(sum(ans))
    print(ans[0])