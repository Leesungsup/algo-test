n,k=map(int,input().split())
m=[[0]*(k+1) for _ in range(n)]
item=[]
for i in range(n):
    item.append(list(map(int,input().split())))
for i in range(n):
    for j in range(1,k+1):
        w=item[i][0]
        v=item[i][1]
        if j>w:
            m[i][j]=max(v+m[i-1][j-w],m[i-1][j])
        else:
            m[i][j]=m[i-1][j]
print(m[n-1][k])

import sys

def knapsack(W, wt, val, n): #W 무게 한도, wt 각 보석 무게, val 각 보석 가격, n 보석 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0;
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            #print(K[i][w], end=' ')
        #print('\n')
    return K[n][W]

wt = []
val = []
N,K = map(int,sys.stdin.readline().strip().split())
for i in range(N):
    w,v = map(int, sys.stdin.readline().strip().split())
    wt.append(w)
    val.append(v)
print(knapsack(K,wt, val, N))