def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
    prev = -1
    for i,ar in enumerate(arr):
        if ar != prev:
            answer.append(ar)
            prev = ar
    
    return answer