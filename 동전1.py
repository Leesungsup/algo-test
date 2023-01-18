n,k=map(int,input().split())
arr=[]
count=0
dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(arr[i],k):
        dp[j]=dp[i]+dp[j-i]
print(dp[k])