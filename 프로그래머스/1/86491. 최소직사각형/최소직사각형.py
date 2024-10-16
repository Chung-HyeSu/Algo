def solution(sizes):
    garo_fin = -21e8
    sero_fin = -21e8
    
    for wallet in sizes:
        garo, sero = max(wallet), min(wallet)
        garo_fin = max(garo_fin, garo)
        sero_fin = max(sero_fin, sero)
    
    answer = garo_fin * sero_fin 
    
    
    return answer