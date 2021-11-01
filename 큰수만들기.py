from itertools import combinations
from itertools import permutations
def solution(number, k):
    answer = ''
    s=list(number)
    max=-987654321
    for j in combinations(s,len(s)-k):
        num=''.join(j)
        if max<int(num):
            max=int(num)
            d=num
    answer=d
    print(answer)
    return answer
solution("1924",2)