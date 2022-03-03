from collections import Counter

def solution(a):
    answer = -1
    if len(a) <= 1:
        return 0
    c = Counter(a)
    print(c)
    for k, v in c.items():
        print(k,v)
        if c[k]*2 < answer:
            continue
        idx = 0
        max_value = k
        length = 0
        while idx < len(a)-1:
            if (a[idx] != max_value and a[idx+1] != max_value) or a[idx] == a[idx+1]:
                idx += 1
                continue
            length += 2
            idx += 2
        answer = max(answer, length)
    return answer
solution([0,3,3,0,7,2,0,2,2,0])
