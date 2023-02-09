import math,sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
start = 1
end=arr[n-1] - arr[0]

if c == 2:
    print(arr[n-1] - arr[0])
else:
    while(start < end):
        mid = (start + end)//2
        count = 1
        ts = arr[0]
        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if arr[i] - ts >= mid:
                count+=1
                ts = arr[i]
        if count >= c:
            answer = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(answer)