def solution(s):
    st = []
    for p in s:
        if p == "(":
            st.append(p)
            
        elif p == ")":
            try:
                st.pop()
            except IndexError:
                return False
            
    return len(st) == 0