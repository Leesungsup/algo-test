for test_case in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    answer=0
    for i in range(0,n,3):
        if len(arr[i:i+3])==3:
            answer+=sum(arr[i:i+2])
        else:
            answer+=sum(arr[i:i+3])
    print("#{} {}".format(test_case,answer))
