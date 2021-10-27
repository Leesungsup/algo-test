from collections import deque
import heapq
def solution(jobs):
    answer=0
    now=0
    start=-1
    i=0
    heap=[]
    while i<len(jobs):
        for job in jobs:
            if start<job[0]<=now :
                heapq.heappush(heap,(job[1],job[0]))
        if 0<len(heap):
            dist,time=heapq.heappop(heap)
            start=now
            now+=dist
            answer+=(now-time)
            i+=1
        else:
            now+=1

