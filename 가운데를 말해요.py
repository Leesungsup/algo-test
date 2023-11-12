import sys
import heapq
n=int(sys.stdin.readline())
leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])

n=int(input())
count=0
me=-10001
for i in range(n):
    count+=1
    k=int(input())
    if count==1:
        me=k
    elif count%2!=0:
        if me<k:
            me=k
    elif count%2==0:
        if me>k:
            me=k
    print(me)