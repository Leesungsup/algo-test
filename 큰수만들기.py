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
def solution1(number,k):
    answer=''
    numbers=list(number)
    stack=[]
    for i in numbers:
        if not stack:
            stack.append(i)
        if k>0:
            while stack[-1]<i:
                stack.pop()
                k-=1
                if not stack and k<=0:
                    break
        stack.append(i)
    return answer
solution("1924",2)