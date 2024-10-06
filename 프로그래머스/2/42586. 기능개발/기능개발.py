from collections import deque
def solution(progresses, speeds):
    answer = []

    q = deque()
    q.append(progresses)
    n = len(progresses)
    finished = [False] * n
    idx = 0

    while q:
        pro = q.popleft()
        if pro[idx] >= 100 and not finished[idx]:
            cnt = 0
            for i in range(idx, n):
                if pro[i] >= 100:
                    cnt += 1
                    idx = i + 1
                    finished[i] = True
                elif pro[i] < 100:
                    break
            answer.append(cnt)

        if finished.count(True) == n:
            break

        for i in range(n):
            if progresses[i] < 100 and not finished[i]:
                progresses[i] += speeds[i]
        q.append(progresses)

    return answer