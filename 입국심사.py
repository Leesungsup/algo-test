def solution(n,times):
    answer=0
    left=0
    right=max(times)*n
    while left<right:
        mid=(left+right)//2
        people=0
        for i in times:
            people+=mid//i
            if people>=n:
                break
        if people>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return answer
def solution1(n,times):
    answer=0
    left=0
    right=max(times)*n
    while left<right:
        mid=(left+right)//2
        people=0
        for i in times:
            people+=mid//i
            if people>=n:
                break
        if people>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    return answer