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
    stack=[]
    numbers=list(number)
    for num in numbers:
        if not stack:
            stack.append(num)
            continue
        if k>0:
            while int(stack[-1])<int(num):
                stack.pop()
                k-=1
                if not stack or k<=0:
                    break
        stack.append(num)
    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)
solution("1924",2)