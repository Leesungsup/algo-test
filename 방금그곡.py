from datetime import datetime
s1 = '0:15'
s2 = '11:15' # for example
FMT = '%H:%M'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
k=str(tdelta)
#print(k[:5])
def solution(m, musicinfos):
    answer = ''
    FMT = '%H:%M'
    arr=[]
    max=-987654321
    for i in musicinfos:
        arr.append(i.split(','))
    am=[]
    for j in range(len(m)):
        if j+1<len(m):
            if m[j+1]=='#':
                am.append(m[j]+m[j+1])
            elif m[j]!='#':
                am.append(m[j])
    if m[-1]!='#':
        am.append(m[-1])
    #print(am)
    #print(arr)
    for i in arr:
        tdelta=datetime.strptime(i[1],FMT)-datetime.strptime(i[0],FMT)
        c=str(tdelta)
        #print(c)
        for j in range(len(c)):
            if c[j]==':':
                #print(c[:j])
                h=int(c[:j])*60
                break
        #print(h+int(c[j+1:j+3]))
        music=[]
        time=h+int(c[j+1:j+3])
        #print(len(i[3]))
        r=[]
        for j in range(len(i[3])):
            if j+1<len(i[3]):
                if i[3][j+1]=='#':
                    r.append(i[3][j]+i[3][j+1])
                elif i[3][j]!='#':
                    r.append(i[3][j])
        if i[3][-1]!='#':
            r.append(i[3][-1])
        #print(r)
        count=i[3].count('#')
        for j in range(time):
            #print(j%len(i[3]))
            #print(r[j%len(r)])
            music.append(r[j%len(r)])
        #print(music)
        for j in range(len(music)):
            num=0
            for k in range(len(am)):
                if j+k>=len(music):
                    num=1
                    break
                if am[k]!=music[j+k]:
                    print(am[k],music[j+k])
                    num=1
                    break
            if num==0:
                if max<time:
                    max=time
                    answer=i[2]
    if answer=='':
        answer='(None)'
    print(answer)
    return answer
solution("A#", ["12:00,12:01,HELLO,A#"])
