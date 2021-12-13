from collections import defaultdict
import math
def solution(str1, str2):
    answer = 0
    s1=[str1[i:i+2] for i in range(0,len(str1)) if len(str1[i:i+2])==2]
    s2=[str2[i:i+2] for i in range(0,len(str2)) if len(str2[i:i+2])==2]
    ds1=dict()
    ds2=dict()
    for i in range(len(s1)):
        if s1[i].isalpha():
            if s1[i].upper() not in ds1:
                ds1[s1[i].upper()]=1
            else:
                ds1[s1[i].upper()]+=1
    for j in range(len(s2)):
        if s2[j].isalpha():
            if s2[j].upper() not in ds2:
                ds2[s2[j].upper()]=1
            else:
                ds2[s2[j].upper()]+=1
    m1=0
    m2=0
    print(ds1,ds2)
    if len(ds1)==0 and len(ds2)==0:
        answer=1
        return answer*65536
    for i in ds2:
        if ds1.get(i):
            m1+=min(ds1[i],ds2[i])
            m2+=max(ds1[i],ds2[i])
            ds1[i]=0
            ds2[i]=0
        else:
            m2+=ds2[i]
    for i in ds1:
        m2+=ds1[i]
    print(m1,m2)
    answer=m1/m2*65536
    print(math.trunc(answer))
    return math.trunc(answer)
solution("handshake","shake hands")
