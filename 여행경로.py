from collections import defaultdict
def solution(tickets):
    answer=[]
    d=defaultdict(list)
    for i in tickets:
        d[i[0]].append(i[1])
    for i in d.keys():
        d[i[0]].sort(reverse=True)
    stack=['ICN']
    while stack:
        tmp=stack[-1]
        if not d[tmp]:
            answer.append(stack.pop)
        else:
            stack.append(d[tmp].pop())
    answer.reverse()
    return answer