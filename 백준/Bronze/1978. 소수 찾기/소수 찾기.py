N = int(input())
arr = list(map(int,input().split()))
ans = 0
for a in arr:
    cnt = 0
    for i in range(1,a+1):
        if a%i == 0:
            cnt +=1
    if cnt == 2:
        ans += 1
print(ans)