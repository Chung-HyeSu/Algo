n = int(input())
ans = 0
for i in range(max(1,n-9*(len(str(n)))), n):
    if i +sum(map(int,str(i))) == n:
        ans = i
        break

print(ans)
