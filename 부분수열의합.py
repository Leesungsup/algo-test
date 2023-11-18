from itertools import combinations
from itertools import permutations
def solution(idx,sum):
    global answer
    temp=sum+a[idx]
    if temp==k:
        answer+=1
        return
    if idx==n:
        if temp==k:
            answer+=1
        return
    if temp>k:
        return
    solution(idx+1,sum)
    solution(idx+1,temp)

T=int(input())

for test_case in range(T):
    answer=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    solution(0,0)
    print("#{} {}".format(test_case,answer))