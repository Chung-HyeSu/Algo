#10818
present = 0
station = 0
Max_present = -21e8

for _ in range(10):
    down, up = map(int,input().split())
    predown_present = present - down
    preup_present = present + up

    if predown_present<=0 :
        present = 0
    else:
        present -= down

    if preup_present >= 10000:
        present = 10000
    else:
        present += up

    Max_present = max(present, Max_present)


print(Max_present)