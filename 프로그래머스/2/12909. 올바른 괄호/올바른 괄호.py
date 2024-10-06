def solution(s):
    
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == ")" and len(stack) == 0:
            return False
        elif p == ")" and p != stack.pop():
            return False
    
    if len(stack) != 0 :
        return False
    else:
        return True