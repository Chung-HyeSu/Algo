def solution(a, b, c, d):
    nums = [0,0,0,0,0,0,0]

    nums[a] += 1
    nums[b] += 1
    nums[c] += 1
    nums[d] += 1

    p,q,r,s = 0,0,0,0

    if 4 in nums:
        for i in range(1,7):
            if nums[i] == 4:
                p = i
        return 1111*p
    elif 3 in nums:
        for i in range(1,7):
            if nums[i] == 3:
                p = i
            elif nums[i] == 1:
                q = i
        return ((10*p+q)**2)
    elif 2 in nums:
        for i in range(1,7):
            if nums[i] == 0:
                continue
            if nums[i] == 2 and p == 0:
                p = i
            elif nums[i] == 2 and p != 0:
                q = i
            elif nums[i] == 1 and r == 0 :
                r = i
            elif nums[i] == 1 and r != 0:
                s = i
        if q != 0 :
            return (p+q)*abs(p-q)
        else :
            return r*s
    else :
        result = 10
        for i in range(1,7):
            if nums[i] != 0:
                result = min(result, i)
        return result
