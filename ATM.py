import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
dp=[0]*(n+1)
for i in range(n):
    dp[i+1]=dp[i]+arr[i]
print(sum(dp))