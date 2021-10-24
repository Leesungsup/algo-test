def solution(name):
    answer=0
    n=len(name)
    for i,k in enumerate(name):
        answer+=min(ord(k)-ord('A'),ord('Z')-ord(k)+1)
        next=i+1
        while next<len(name) and name[next]=='A':
            next+=1
        n=min(n,i+i+len(name)-next)
    answer+=n