# import heapq
# import sys
# n=int(sys.stdin.readline())
# q=[]
# for i in range(n):
#     n=int(sys.stdin.readline())
#     if n==0:
#         if len(q)==0:
#             print(0)
#         else:
#             x=heapq.heappop(q)
#             print(x*-1)
#     else:
#         heapq.heappush(q,(-n))
#
# import heapq
# import sys
# n=int(sys.stdin.readline())
# q=[]
# for i in range(n):
#     n=int(sys.stdin.readline())
#     if n==0:
#         if len(q)==0:
#             print(0)
#         else:
#             x=heapq.heappop(q)
#             print(x)
#     else:
#         heapq.heappush(q,(n))

import heapq
import sys
n=int(sys.stdin.readline())
q=[]
for i in range(n):
    n=int(sys.stdin.readline())
    if n==0:
        if len(q)==0:
            print(0)
        else:
            x,y=heapq.heappop(q)
            print(x*y)
    else:
        if n>0:
            heapq.heappush(q,(n,1))
        else:
            heapq.heappush(q,(n*-1,-1))