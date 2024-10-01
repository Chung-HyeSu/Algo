lst = [int(input()) for _ in range(9)]
lst.sort()

all = sum(lst)
a,b = 0,0

for i in range(8):
    for j in range(i+1,9):
        if all - (lst[i]+ lst[j]) == 100:
            a,b = i,j


for i in range(len(lst)):
    if i != a and i != b:
        print(lst[i])
