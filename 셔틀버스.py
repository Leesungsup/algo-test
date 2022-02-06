import datetime
from collections import defaultdict
def solution(n, t, m, timetable):
    answer = ''
    d = defaultdict(list)
    FMT='%H:%M'
    time=datetime.datetime.strptime('09:00',FMT)
    timetable.sort(key=lambda x: datetime.datetime.strptime(x,FMT))
    #print(timetable)
    d['09:00']=[]
    #print(d)
    for i in range(1,n):
        #print(i)
        ktime=time+datetime.timedelta(minutes=t)
        k=str(ktime)
        #print(k)
        k=k.split(' ')
        d[k[1][:5]]=[]
        time=ktime
    #print(d)
    for j in d:
        mun=0
        for i in timetable:
            #print(i)
            if datetime.datetime.strptime(j, FMT) >= datetime.datetime.strptime(i, FMT):
                d[j].append(i)
                mun+=1
            if mun==m:
                break
        for i in range(mun):
            timetable.remove(d[j][i])
    #print(d)
    kanswer=''
    o=0
    for i in d:
        o+=1
        if o==len(d) and len(d[i])<m:
            answer=i
    if answer=='':
        for i in d:
            for j in d[i]:
                kanswer=datetime.datetime.strptime(j,FMT)-datetime.timedelta(minutes=1)
    if kanswer!='':
        k=str(kanswer)
        k=k.split(' ')
        answer=k[1][:5]
    #print(answer)
    return answer