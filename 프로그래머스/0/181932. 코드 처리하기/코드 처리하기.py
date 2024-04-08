# 코드 처리하기
def solution(code):
    answer = ''
    mode = True

    for idx in range(len(code)):
        if code[idx] == '1':
            mode = not mode
            continue
        elif mode and idx%2 == 0 :
            answer = answer + code[idx]
        elif mode == False and idx%2 == 1:
            answer = answer + code[idx]
            
    if len(answer) == 0:
        return "EMPTY"
    else :
        return answer