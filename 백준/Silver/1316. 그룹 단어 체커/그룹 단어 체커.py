#그룹단어
n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    lst = []
    num = 0
    for i in range(len(word)):
        if word[i] not in lst:
            lst.append(word[i])
        elif word[i] in lst and word[i-1] == word[i]:
            num+=1
        elif word[i] in lst and word[i-1] != word[i]:
            break
        if len(lst)+num == len(word):
            cnt+=1



print(cnt)
