from itertools import combinations
T=int(input())
for i in range(1,T+1):
    s=list(input())
    stack=[]
    p=[]
    answer=set()
    for j,c in enumerate(s):
        if c=='(':
            stack.append(j)
        if c==')':
            p.append((stack.pop(),j))
    for j in range(1,len(p)+1):
        c=combinations(p,j)
        for k in c:
            s1=s[:]
            print(s1,k)
            for h1,h2 in k:
                s1[h1]=''
                s1[h2]=''
                print(h1,h2,s1)
            answer.add(''.join(map(str,s1)))
