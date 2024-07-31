t = int(input())
ans = [0,1]

if t>=2:
    for i in range(2,t+1):
        ans.append(ans[i-2]+ans[i-1])
    print(ans[-1])
else:
    print(ans[t])