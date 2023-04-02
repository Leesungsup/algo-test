import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)] #11
start, end = 1, max(lan) #이분탐색 처음과 끝위치
while start <= end: #적절한 선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    print('mid:',mid, end=" ")
    lines = 0 #선 수
    for i in lan:
        lines += i // mid #분할 된 선 수
        print('lines:',lines)

    if lines >= N: #선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print('end:',end)

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
start=min(arr)
end=max(arr)
answer=-1
while start<end:
    print(start)
    print(end)
    middle=(start+end)//2
    s=0
    for i in range(n):
        s+=arr[i]//middle
        print(arr[i]//middle)
    print(s)
    if s>=m:
        start=middle+1
        if answer<middle:
            answer=middle
    else:
        end=middle-1
    print(answer)

from bisect import bisect_left, bisect_right
def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i
nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]
# 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()  # 정렬은 필수
print(calCountsByRange(nums, 5, 7))
def binarysearch(target,start,end,arr):
    middle=(start+end)//2
    if target==arr[middle]:
        return middle
    if target<arr[middle]:
        binarysearch(target,start,middle-1,arr)
    elif target>arr[middle]:
        binarysearch(target,middle+1,end,arr)

def binarysearch(target,start,end,arr):
    if start>end:
        return
    while start<end:
        middle=(start+end)//2
        if arr[middle]==target:
            answer=middle
            break;
        if arr[middle]<target:
            start=middle+1
        elif arr[middle]>target:
            end=middle-1
    return arr[answer]
def quick(start,end,arr):
    if start>=end:
        return arr
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and arr[pivot]>=arr[left]:
            left+=1
        while right>start and arr[pivot]<=arr[right]:
            right-=1,
        if left>right:
            arr[pivot],arr[right]=arr[right],arr[pivot]
        else:
            arr[left],arr[right]=arr[right],arr[left]
    quick(start,right-1,arr)
    quick(right+1,end,arr)
    return arr
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=quick(0,len(a)-1,a)
answer=0
for i in range(len(a)):
    m=-987654321
    for j in range(len(b)):
        if m<b[j]:
            m=b[j]
    b.remove(m)
    answer+=a[i]*m
print(answer)