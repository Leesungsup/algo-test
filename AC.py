from collections import deque

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for i in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")


import sys
input = sys.stdin.readline
d1=[]
n=int(input())
for i in range(n):
    d=[]
    q=[]
    k=1
    o=1
    s=input()
    m=int(input())
    if m==0:
        k=-1
    c=input()
    c=c[1:-2]
    c=c.split(',')
    # if c[0]=='':
    #     k=-1
    if k==1:
        for j in c:
            q.append(int(j))
        for j in list(s):
            if j=='R':
                o*=-1
            elif j=='D':
                if len(q)==0:
                    k=-1
                    break
                else:
                    if o==1:
                        d.append(q.pop(0))
                    elif o==-1:
                        d.append(q.pop())
    if k==-1:
        d1.append("error")
    else:
        if o==1:
            d1.append(q)
            #print(q)
        elif o==-1:
            q.reverse()
            d1.append(q)
            #print(q)
for i in d1:
    if i!="error":
        print('['+','.join(map(str, i))+']')
    else:
        print(i)