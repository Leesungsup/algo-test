#1초에 한번에 얼마나 많은 lines의 시간들을 처리할 수 있는 횟수
def throughput(log,start,end):
    cnt=0
    for x in log:
        if x[0] < end and x[1]>=start:
            cnt+=1
    return cnt
def solution(lines):
    answer = 0
    log=[]
    for i in lines:
        date,s,t=lines.split()
        s=s.split(':')
        t=t.split('s','')
        end=(int(s[0])*3600+int(s[1])*60+float(s[2]))*1000
        start=end-float(t)*1000+1
        log.append([start,end])
    for x in log:
        answer=max(answer,throughput(log,x[0],x[0]+1000),throughput(log,x[1],x[1]+1000))
    return answer
