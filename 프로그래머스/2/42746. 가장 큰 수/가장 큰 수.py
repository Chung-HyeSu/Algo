def solution(numbers):
    answer = ''
    
    lst = list(map(str,numbers))
    
    def compare(x):
        #정렬하는 조건
        #문자열을 가지고 하는것
        # 3, 30, 340
        return x * (4//len(x)+1)
        
    sorted_numbers = sorted(lst, key=compare, reverse=True)
    answer = ''.join(sorted_numbers)

    
    
    return answer if int(answer) != 0 else '0'