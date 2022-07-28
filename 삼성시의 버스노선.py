T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=[0]*5001
    for i in range(n):
        a,b=map(int,input().split())
        for j in range(a,b+1):
            arr[j]+=1
    print("#",end="")
    print(test_case,end=" ")
    p=int(input())
    for i in range(p):
        c=int(input())
        print(arr[c],end=" ")
    print()