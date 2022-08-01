T=int(input())
for test_case in range(1,T+1)
    answer=0
    win={}
    lose={}
    n=int(input())
    m=int(input())
    for i in range(1,n+1):
        win[i]=set()
        lose[i]=set()
    results=[]
    for i in range(m):
        a,b=map(int,input().split())
        results.append((a,b))
    for i in range(1,n+1):
        for j in results:
            if i==j[0]:
                win[i].add(j[1])
            if i==j[1]:
                lose[i].add(j[0])
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
    print("#{} {}".format(test_case,answer))
    return answer