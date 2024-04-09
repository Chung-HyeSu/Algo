def solution(rank, attendance):
    award = []
    for i in range(len(rank)):
        if attendance[i] == True:
            award.append([rank[i],i])
            
    award.sort()
    return 10000*award[0][1]+100*award[1][1]+award[2][1]