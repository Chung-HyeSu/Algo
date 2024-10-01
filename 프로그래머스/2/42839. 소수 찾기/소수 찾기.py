from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []

    #종이조각 쪼개기
    for i in range(len(numbers)):
        nums.append(numbers[i])
                    
            
    #nums에서 중복없이 숫자를 뽑아 나올 수 있는 조합 만들기
    combi = set()
    for length in range(1, len(numbers)+1):
        for perm in permutations(nums, length):
            number = int(''.join(perm))
            combi.add(number)
    
     
    
    #소수 거르기
    #combi = {1, 71, 17, 7}
    sosu = set()
    def is_sosu(com):
        if com <=1:
            return False
        for i in range(2,com):
            if com%i == 0:
                return False
        return True
    
    for com in combi:
        if is_sosu(com):
            sosu.add(com)
    
    
    
    return len(sosu)