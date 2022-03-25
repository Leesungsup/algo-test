from collections import deque
def bfs(n,s):
    q=deque(s)
    print(q)
    while q:
        t=q.popleft()
        print(t)
        if t>2**64:
            return 0
        elif t%n==0:
            return t
        q.append(t*10)
        q.append(t*10+1)
def solution(n):
    print(bfs(n,[1]))
solution(3)
def solution1(n):
    b=0b11
    deci=int(format(b,'b'),10)
    print(b)
    print(deci)
    deci=int(format(b,'b'),8)
    print(b)
    print(deci)
    while True:
        deci=int(format(b,'b'),10)
        if deci>2**64:
            return 0
        elif deci%n==0:
            break
        b+=1
    print(deci)
solution1(3)
