from itertools import combinations
from itertools import permutations
import math
def solution3(brown, yellow):
    answer = []
    min=987654321
    for i in range(1,(brown+yellow)//2+1):
        for j in range(1,i+1):
            if i*j>(brown+yellow):
                break
            if i*j==(brown+yellow):
                if (i-2)*(j-2)==yellow:
                    if i-j>=0:
                        if i-j<=min:
                            min=(i-j)
                            answer.append(i)
                            answer.append(j)
    return answer
def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True
def solution2(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in perlist:
            if check(int(i)):
                answer.append(int(i))
    answer = len(set(answer))
    return answer
def solution1(answers):
    answer=[]
    count=[0]*3
    j=[1,2,3,4,5]
    j1=[2,1,2,3,2,4,2,5]
    j2=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if j[i]==answers[i]:
            count[0]+=1
        if j1[i]==answers[i]:
            count[1]+=1
        if j2[i]==answers[i]:
            count[2]+=1
    m=-987654321
    index=0
    for i in range(3):
        if m<count[i]:
            m=count[i]
            index=i
    for i in range(3):
        if count[index]==count[i]:
            answer.append(i)
    return answer
def solution(brown,yellow):
    answer=[]
    for i in range(1,(yellow+brown)//2+1):
        for j in range(1,i):
            if i*j>(yellow+brown):
                break
            if i*j==(yellow+brown):
                if (i-2)*(j-2)==yellow:
                    if i-j>=0:
                        if (i-j)<min:
                            min=(i-j)
                            answer.append(i)
                            answer.append(j)
    return answer