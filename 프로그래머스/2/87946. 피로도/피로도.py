def solution(k, dungeons):
    global visited, max_cnt
    answer = -1
    
    visited = [False]*len(dungeons)
    max_cnt = -21e9
    #최소 필요 피로도 : 탐험 시작하기 위해 최소로 필요로하는 피로도
    #소모 피로도 : 탐험 마쳤을 때 소모되는 피로도
    #80 20 : 탐험하기위해서는 80이상 필요하고, 탐험 후에는 20이 소모됨
    #하루에 한번씩 탐험할 수 있는 던전 많음. 최대한 많이 탐험하려고 함.
    #현재 피로도 k, 각던전별 최소 필요 피로도, 소모 피로도 담긴 2차원 배열 dungeons
    #유저가 탐험할 수 있는 최대 던전수
    
    def explore(power, cnt):
        global max_cnt
        if cnt > max_cnt:
            max_cnt = cnt
        
        for (idx,dun) in enumerate(dungeons):
            if power>=dun[0] and visited[idx] == False:
                visited[idx] = True
                explore(power-dun[1], cnt+1)
                visited[idx] = False
                
                

    explore(k,0)
    
    
    return max_cnt

