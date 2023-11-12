import sys
input = sys.stdin.readline()
#2631
n = int(input())
childeren = [int(input()) for _ in range(n)]

def find(idx):
    s, e = 0, len(lis)-1
    while s < e:
        m = (s+e)//2
        if lis[m] < childeren[idx]:
            s = m+1
        else:
            e = m
    return e

# LIS
lis = []
for i in range(n):
    if not lis or lis[-1] < childeren[i]:
        lis.append(childeren[i])
    elif lis[-1] > childeren[i]:
        lis[find(i)] = childeren[i]

print(n-len(lis))

#7570
n = int(input())
arr= list(map(int,input().split()))
dp=[0]*(n+1)
long=0
for i in range(n):
    idx=arr[i]
    dp[idx]=dp[idx-1]+1
    long=max(dp[idx],dp[idx-1]+1)
print(n-long)