from collections import deque
import sys
sys.stdin=open("input.txt","r")
for test_case in range(1,11):
    n=int(input())
    arr=[]
    q=deque()
    for i in range(16):
        k1=list(map(int,input()))
        #print(k1)
        for j in range(16):
            if k1[j]==2:
                q.append((i,j))
        arr.append(k1)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    k=0
    while q:
        x,y=q.popleft()
        #print(x,y)
        if arr[x][y]==3:
            #print("x,y",x,y)
            k=1
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<16 and ny>=0 and ny<16:
                if arr[nx][ny]==0 or arr[nx][ny]==3:
                    if arr[nx][ny]==0:
                        arr[nx][ny]=1
                    q.append((nx,ny))
    #print(arr)
    print("#{} {}".format(test_case,k))


from collections import deque
import sys
sys.stdin=open("input.txt","r")
for test_case in range(1,11):
    n=int(input())
    arr=[]
    q=deque()
    for i in range(100):
        k1=list(map(int,input()))
        #print(k1)
        for j in range(100):
            if k1[j]==2:
                q.append((i,j))
        arr.append(k1)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    k=0
    while q:
        x,y=q.popleft()
        #print(x,y)
        if arr[x][y]==3:
            #print("x,y",x,y)
            k=1
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<100 and ny>=0 and ny<100:
                if arr[nx][ny]==0 or arr[nx][ny]==3:
                    if arr[nx][ny]==0:
                        arr[nx][ny]=1
                    q.append((nx,ny))
    #print(arr)
    print("#{} {}".format(test_case,k))
