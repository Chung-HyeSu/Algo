import sys
input = sys.stdin.readline

l,c = map(int,input().split())
letters = sorted(list(map(str,input().split())))
moeum = ['a','e','i','o','u']
temp = []

def back(idx, cn_mo, cn_ja):
    if len(temp) == l:
        if cn_mo>=1 and cn_ja>=2:
            print(''.join(temp))
        return

    for i in range(idx,c):
        temp.append(letters[i])
        if letters[i] in moeum:
            back(i+1, cn_mo+1, cn_ja)
        else:
            back(i+1, cn_mo, cn_ja+1)
        temp.pop()


back(0,0,0)