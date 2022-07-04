from itertools import combinations
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    a=[1]+[0]*sum(arr)
    print(a)
    for i in arr:
        for j in range(len(a)-1,-1,-1):
            if a[j]:
                a[j+i]=1
    print(sum(a))
    print("#{} {}".format(test_case,sum(a)))

T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    answer=set()
    arr=list(map(int,input().split()))
    for i in range(n+1):
        c=combinations(arr,i)
        for k in c:
            s=0
            #print(sum(k))
            #sum+=j
            #print(s)
            answer.add(sum(k))
    #print(answer)
    print("#{} {}".format(test_case,len(answer)))

from itertools import combinations
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    answer=set()
    arr=list(map(int,input().split()))
    for i in range(n+1):
        c=combinations(arr,i)
        for k in c:
            s=0
            #print(sum(k))
            #sum+=j
            #print(s)
            answer.add(sum(k))
    #print(answer)
    print("#{} {}".format(test_case,len(answer)))

from itertools import combinations
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    answer=set()
    arr=list(map(int,input().split()))
    for i in range(n+1):
        c=combinations(arr,i)
        for k in c:
            s=0
            #print(sum(k))
            #sum+=j
            #print(s)
            answer.add(sum(k))
    #print(answer)
    print("#{} {}".format(test_case,len(answer)))
