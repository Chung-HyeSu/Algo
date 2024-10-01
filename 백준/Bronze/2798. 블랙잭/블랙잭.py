#n장의 카드 중 3장을 고름.
#m을 넘지 않으면서 m에 가깝게 만들어야함

n,m = map(int,input().split())
cards = list(map(int,input().split()))

max_sum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cur_sum = cards[i]+cards[j]+cards[k]

            if cur_sum <= m and cur_sum > max_sum:
                max_sum = cur_sum

print(max_sum)