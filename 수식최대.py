from itertools import permutations
import re
def solution(expression):
    answer = 0
    r=['*','+','-']
    k=permutations(r,3)
    g=re.split('[0-9]',expression)
    g=''.join(g)
    d=re.split('[*+-]',expression)
    print(d)
    sic=[]
    for i in range(len(g)):
        sic.append(int(d[i]))
        sic.append(g[i])
    sic.append(int(d[-1]))
    sic1=[]
    print(sic)
    mx=0
    for i in k:
        array = sic[:]
        for j in range(3):
            for k in range(0,len(array)-1):
                if array[k] == i[j]:
                    if array[k] == '*':
                        array[k+1] *= array[k-1]
                    elif array[k] == '+':
                        array[k+1] += array[k-1]
                    elif array[k] == '-':
                        array[k+1] = array[k-1] - array[k+1]
                    array[k] = -1
                    array[k-1] = -1
            a = []
            for k in array:
                if k != -1:
                    a.append(k)
            array = a[:]
        print(array)
        mx = max(mx,abs(array[0]))
    answer = mx

    for i in k:
        sic1=sic[:]
        print(sic1)
        num=0
        g1=-1
        print(i)
        for j in i:
            num+=1
            for p in range(len(sic)):
                if sic[p]==j:
                    if j=='*':
                        s=int(sic1[p-1])*int(sic1[p+1])
                        sic1[p-1]=str(s)
                        sic1[p]=str(s)
                        sic1[p+1]=str(s)
                        if p==len(sic)-1 and num==3:
                            g1=p
                    elif j=='+':
                        s=int(sic1[p-1])+int(sic1[p+1])
                        sic1[p-1]=str(s)
                        sic1[p]=str(s)
                        sic1[p+1]=str(s)
                        if p==len(sic)-1 and num==3:
                            g1=p
                    else:
                        s=int(sic1[p-1])-int(sic1[p+1])
                        sic1[p-1]=str(s)
                        sic1[p]=str(s)
                        sic1[p+1]=str(s)
                        if p==len(sic)-1 and num==3:
                            g1=p
        print(sic1[g1])
        print(sic1)
    return answer
solution("100-200*300-500+20")
