from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 일차선 다리. 모든 트럭이 다리를 건너려면 최소 몇초.
    # bridge_length: 다리길이, 올라갈 수 있는 트럭수
    # weight: 견딜 수 있는 무게 / truck_weights: 트럭별 무게 / 전부 1이상 10000이하
    # 모든 트럭의 무게는 1이상 weight 이하 == 건널 수 없는 트럭은 없음

    q = deque(truck_weights)
    b = deque()
    time = 0
    cur_wei = 0  # 현재트럭무게

    while q or b:
        if b and b[0][1] >= bridge_length:
            cur_wei -= b[0][0]
            b.popleft()

        for i in range(len(b)):
            truck, location = b[i]
            if location < bridge_length:
                b[i] = [truck, location + 1]

        if q and cur_wei + q[0] <= weight and len(b) < bridge_length:
            truck = q.popleft()
            cur_wei += truck
            b.append([truck, 1])

        time += 1

    return time