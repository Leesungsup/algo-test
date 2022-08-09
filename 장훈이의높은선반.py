from itertools import combinations
T=int(input())
for test_case in range(1,T+1):
    n,b=map(int,input().split())
    arr=list(map(int,input().split()))
    carr=[]
    min=987654321
    count=0
    for i in range(n+1,1,-1):
        if count >=5:
            break
        carr=combinations(arr,i)
        for j in carr:
            if sum(j)>=b:
                count=0
                if min>b-sum(j):
                    min=b-sum(j)
            else:
                count+=1
    print("#{} {}".format(test_case,min))
