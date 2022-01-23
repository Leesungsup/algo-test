from itertools import combinations
def solution(arr):
    answer = 0
    arr.sort(reverse=True)
    num=0
    for i in range(1,len(arr)):
        if arr[0]%arr[i]!=0:
            num=1
    if num==0:
        return arr[0]
    min=int(1e9)
    for i in range(2,len(arr)+1):
        c=list(combinations(arr,i))
        for j in c:
            d=1
            for k in j:
                d*=k
            num=0
            for k in arr:
                #print(j[0]*j[1])
                if d%k!=0:
                    num=1
            if num==0 and min>d:
                min=d
    print(min)
    return min
import math
def solution1(arr):
    answer=0
    k=1
    for i in arr:
        k=math.lcm(k,i)
        print(k)
    return k
solution1([2,6,8,14])
def solution2(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        while a%b:
            r = a%b
            a = b
            b = r
        arr[i+1] = (arr[i]*arr[i+1])/b
    return arr[-1]
