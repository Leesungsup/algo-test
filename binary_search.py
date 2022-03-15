def binary_search(array,start,end,target):
    while start<end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
def quick(array,start,end):
    if start>=end:
        return array
    pivot=start
    left=start+1
    right=end
    while left<=right:
        if array[pivot]>=array[left] and left<=end:
            left+=1
        elif array[pivot]<array[right] and right>start:
            right-=1
        if left<right:
            array[left],array[right]=array[right],array[left]
        else:
            array[pivot],array[right]=array[right],array[pivot]
    quick(array,start,right-1)
    quick(array,right+1,end)
    return array