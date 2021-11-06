def solution1(name):
    answer=0
    n=len(name)
    for i,k in enumerate(name):
        answer+=min(ord(k)-ord('A'),ord('Z')+ord(k)+1)
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1
        n=min(n,i+i+len(name)-next)
    answer+=n
    return answer
def solution(n,lost,reserve):
    answer=0
    lost_set=set(lost)-set(reserve)
    reserve_set=set(reserve)-set(lost)
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    answer=n-len(lost_set)
    return answer