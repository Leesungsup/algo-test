def solution(distance,rocks,n):
    answer=0
    rocks.sort()
    rocks.append(distance)
    left=0
    right=distance
    while left<=right:
        mid=(left+right)//2
        mid_distance=987654321
        cur=0
        remo=0
        for i in rocks:
            diff=i-cur
            if diff<mid:
                remo+=1
            else:
                cur=i
                mid_distance=min(mid_distance,diff)
        if remo>n:
            right=mid-1
        else:
            left=mid+1
            answer=mid_distance
    return answer