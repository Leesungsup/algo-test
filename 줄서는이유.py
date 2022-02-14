from itertools import permutations
def solution(n, k):
    answer = []
    d=[i for i in range(1,n+1)]
    q=list(permutations(d,3))
    print(q[k-1])
    for i in q[k-1]:
        answer.append(i)
    return answer
solution(3,5)
from math import factorial
def solution(n, k):
    answer = []
    nl = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        answer.append(nl.pop((k-1)//fact))
        n -= 1
        k %= fact
    return answer
