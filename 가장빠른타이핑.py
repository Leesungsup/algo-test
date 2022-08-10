T=int(input())
for test_case in range(1,T+1):
    a,b=map(str,input().split())
    time=0
    i=0
    while True:
        if i==len(a):
            break
        k=0
        print(a[i:i+len(b)])
        if a[i:i+len(b)]!=b:
            k=1
        if k==0:
            time+=1
            i+=len(b)
        else:
            i+=1
            time+=1
    print("#{} {}".format(test_case,time))
