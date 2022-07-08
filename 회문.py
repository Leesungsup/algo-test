
for test_case in range(1,11):
    n=int(input())
    arr=[]
    num=0
    for i in range(8):
        arr.append(list(input()))
    #print(arr)
    for i in range(8):
        for j in range(8):
            if i+n-1<8:
                r=[]
                r1=[]
                for k in range(n):
                    r+=arr[i+k][j]
                r1=list(reversed(r))
                if ''.join(r)==''.join(r1):
                    num+=1
            if j+n-1<8:
                d=[]
                d1=[]
                for k in range(n):
                    d+=arr[i][j+k]
                d1=list(reversed(d))
                if ''.join(d)==''.join(d1):
                    num+=1
    print("#{} {}".format(test_case,num))
