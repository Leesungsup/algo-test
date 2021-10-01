from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q=deque()
    time=0
    for i in range(bridge_length):
        q.append(0)
    while q:
        time+=1
        q.popleft()
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    answer=time
    return answer