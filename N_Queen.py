T=int(input())
arr=[[0]*8 for _ in range(8)]
def able(x,y):
    ret_num=1
    for i in range(n):
        if arr[i][y]==1:
            ret_num=0
    for j in range(n):
        if arr[x][j]==1:
            ret_num=0
    if x>=y:
        for i in range(n):
            for j in range(n):
                if i-j==x-y:
                    if arr[i][j]==1:
                        ret_num=0
    else:
        for i in range(n):
            for j in range(n):
                if j-i==y-x:
                    if arr[i][j]==1:
                        ret_num=0
    for i in range(n):
        for j in range(n):
            if i+j==x+y:
                if arr[i][j]==1:
                    ret_num=0
    return ret_num
def check(depth):
    global result
    global cnt
    if depth==n:
        cnt+=1
        result=cnt
        return 1
    for i in range(n):
        if able(i,depth)==1:
            arr[i][depth]=1
            check(depth+1)
        arr[i][depth]=0
    return 0
for i in range(1,T+1):
    n=int(input())
    result=0
    cnt=0
    check(0)
    print('#{} {}'.format(i, result))
