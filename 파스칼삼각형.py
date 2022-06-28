T=int(input())
for i in range(1,T+1):
    n=int(input())
    arr=[[1]*j for j in range(1,n+1)]
    for j in range(1,n):
        for k in range(j+1):
            if k==0:
                continue
            elif k==j:
                continue
            else:
                arr[j][k]=arr[j-1][k-1]+arr[j-1][k]
    print("#{}".format(i))
    for j in range(n):
        for k in range(j+1):
            print(arr[j][k],end=" ")
        print()
