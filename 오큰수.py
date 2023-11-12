from collections import deque
n=int(input())
a=list(map(int,input().split()))
q=deque()
answer=[-1]*n
for i in range(n):
    while q and (q[-1][0] < a[i]):
        number,index=q.pop()
        answer[index]=q[i]
    q.append((a[i],i))
print(answer)