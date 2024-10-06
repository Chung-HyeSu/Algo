def solution(word):
    answer = []
    mouem = ['A', 'E', 'I', 'O', 'U']

    # 어차피 단어의 수가 많지 않음. 다 만들어서 정렬
    def make_words(cur, length):
        if length == 0:
            answer.append(cur)
            return

        for mo in mouem:
            make_words(cur + mo, length - 1)

    for leng in range(1, 6):
        make_words('', leng)

    answer.sort()

    return answer.index(word) + 1