n = input()
ans = 0
for i in range(1,len(n)):
    ans += int('9'+(i-1)*'0')*i

ans += (int(n)-10**(len(n)-1)+1)*len(n)

print(ans)