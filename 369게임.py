T=int(input())
for i in range(1,T+1):
    arr=list(str(i))
    a=0
    for j in arr:
        if int(j)!=0 and int(j)%3==0:
            print("-",end="")
            a=1
    if a==1:
        print("",end=" ")
    if a==0:
        print(i,end=" ")