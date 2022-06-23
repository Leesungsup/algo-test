import heapq
for i in range(1,11):
    n=int(input())
    di=0
    arr=list(map(int,input().split()))
    heap=[]
    for num in arr:
        heapq.heappush(heap, num*-1)
    heapq.heapify(arr)
    for j in range(n):
        mi=heapq.heappop(arr)
        ma=heapq.heappop(heap)
        #arr.remove(ma*-1)
        #heap.remove(mi*-1)
        #print(ma)
        #print(mi)
        ma=ma*-1
        ma-=1
        mi+=1
        #print(ma)
        #print(mi)
        heapq.heappush(arr,mi)
        #heapq.heappush(arr,ma)
        heapq.heappush(heap,ma*-1)
        #heapq.heappush(heap,mi*-1)
    mi=heapq.heappop(arr)
    ma=heapq.heappop(heap)
    print(arr)
    print(heap)
    ma=ma*-1
    di=ma-mi
    print("#{} {}".format(i,di))
