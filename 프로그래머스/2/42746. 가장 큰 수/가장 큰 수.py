def solution(numbers):
    lst = list(map(str,numbers))
    
    def compare(x):
        return x*(4//len(x)+1)
        
    a = sorted(lst, key = compare, reverse=True)
    answer = ''.join(a)
    
    
    return answer if int(answer) != 0 else '0'