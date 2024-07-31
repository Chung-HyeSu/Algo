#2309
lst = [int(input()) for _ in range(9)]

flag = True
for i in range(9):
    if flag:
        for j in range(i+1, 9):
            ex_1 = lst[i]
            ex_2 = lst[j]

            if sum(lst) - ex_1 - ex_2 == 100:
                lst.remove(ex_1)
                lst.remove(ex_2)
                flag = False
                break

print(*sorted(lst), sep='\n')