from collections import deque
d=[]
arr=[]
q=deque()
n=int(input())
for i in range(n):
    s=input()
    if 'push' in s.split():
        q.append(s.split()[1])
    elif 'pop' in s.split():
        if len(q)==0:
            d.append(-1)
        else:
            d.append(q.popleft())
    elif 'back' in s.split():
        if len(q)==0:
            d.append(-1)
        else:
            d.append(q[-1])
    elif 'front' in s.split():
        if len(q)==0:
            d.append(-1)
        else:
            d.append(q[0])
    elif 'empty' in s.split():
        if len(q)==0:
            d.append(1)
        else:
            d.append(0)
    elif 'size' in s.split():
        d.append(len(q))
for i in d:
    print(i)