T=int(input())
for i in range(1,T+1):
    arr=[]
    for _ in range(9):
        arr.append(list(map(int,input().split())))
    for j in range(9):
        di=dict()
        s=1
        for k in range(9):
            if arr[j][k] in di:
                s=0
                break
            elif arr[j][k] not in di:
                di[arr[j][k]]=1
        if s==0:
            break
        else:
            s=1
            di=dict()
            for k in range(9):
                if arr[k][j] in di:
                    s=0
                    break
                elif arr[k][j] not in di:
                    di[arr[k][j]]=1
            if s==0:
                break
    if s==1:
        for j in range(0,9,3):
            for k in range(0,9,3):
                di=dict()
                s=1
                for j1 in range(3):
                    for k1 in range(3):
                        if arr[j+j1][k+k1] in di:
                            s=0
                            break
                        elif arr[j+j1][k+k1] not in di:
                            di[arr[j+j1][k+k1]]=1
                    if s==0:
                        break
                if s==0:
                    break
            if s==0:
                break
    print("#{} {}".format(i,s))
