def solution(stones, k):
    answer = 0
    n=0
    out=[]
    start_pos=0
    #min=987654321
    for idx in range(start_pos, len(stones)):
        g=stones[start_pos:start_pos + k]
        if len(g)==k:
            out.append(max(g))
        start_pos = start_pos + 1
    #print(out)
    #for i in out:
    #    if min>max(i):
    #        min=max(i)
    #print(min(out))
    return min(out)
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)
import copy
def solution(stones,k):
    left=1
    right=max(stones)
    while left<=right:
        temp=copy.deepcopy(stones)
        mid=(left+right)//2
        cnt=0
        for t in temp:
            if t<=mid:
                cnt+=1
            else:
                cnt=0
        if cnt>=k:
            right=mid-1
        else:
            left=mid+1
    return left
