import copy
T=int(input())
for test_case in range(1,T+1):
    bin=input()
    thr=input()
    barr=[]
    tarr=[]
    for i in range(len(bin)):
        bin1=list(copy.deepcopy(bin))
        if bin1[i]=='0':
            bin1[i]='1'
            barr.append(int(''.join(bin1),2))
        elif bin1[i]=='1':
            bin1[i]='0'
            barr.append(int(''.join(bin1),2))
    for i in range(len(thr)):
        thr1=list(copy.deepcopy(thr))
        if thr1[i]=='0':
            thr1[i]='1'
            tarr.append(int(''.join(thr1),3))
            thr1[i]='2'
            tarr.append(int(''.join(thr1),3))
        elif thr1[i]=='1':
            thr1[i]='0'
            tarr.append(int(''.join(thr1),3))
            thr1[i]='2'
            tarr.append(int(''.join(thr1),3))
        elif thr1[i]=='2':
            thr1[i]='0'
            tarr.append(int(''.join(thr1),3))
            thr1[i]='1'
            tarr.append(int(''.join(thr1),3))
    #print(barr)
    #print(tarr)
    for i in range(len(barr)):
        for j in range(len(tarr)):
            if int(barr[i])==int(tarr[j]):
                answer=int(barr[i])
                break
    print("#{} {}".format(test_case,answer))
