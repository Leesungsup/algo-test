def solution(nums):
    answer = 0
    d=dict()
    for i in nums:
        if i not in d:
            d[i]=1
    print(d)
    print(len(d))
    if len(nums)//2<len(d):
        answer=len(nums)//2
    else:
        answer=len(d)
    print(answer)
    return answer
solution([3,1,2,3])
