def sokution2(distance,rocks,n):
    answer=0
    rocks.sort()
    rocks.append(distance)
    left=0
    right=distance
    while left<right:
        mid=(left+right)//2
        mid_distance=987654321
        remo=0
        cur=0
        for i in rocks:
            diff=i-cur
            if mid>diff:
                remo+=1
            else:
                cur=i
                mid_distance=min(mid_distance,diff)
        if remo>n:
            right=mid-1
        else:
            answer=mid_distance
            left=mid+1
    return answer
def solution1(n,times):
    answer=0
    right=max(times)*n
    left=1
    while left<right:
        mid=(left+right)//2
        people=0
        for i in times:
            people+=mid//i
            if people>=n:
                break
        if people>=n:
            right=mid-1
            answer=mid
        else:
            left=mid+1
    return answer
def quick(array,start,end):
    if start>=end:
        return
    left=start+1
    right=end
    pivot=start
    while left<=right:
        while array[left]<=array[pivot] and left<=end:
            left+=1
        while array[right]>=array[pivot] and right>start:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[right],array[left]=array[left],array[right]
    quick(array,right+1,end)
    quick(array,start,right-1)
    return array
def quick(array,start,end):
    if start>=end:
        return array
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    quick(array,start,right-1)
    quick(array,right+1,end)
    return array
def solution(n,times):
    answer=0
    right=max(times)*n
    left=0
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
def solution1(distance,rocks,n):
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