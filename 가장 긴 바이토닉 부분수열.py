x = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(x)]
dp1 = [1 for j in range(x)]
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
max_dp = max(dp)
for i in range(x-1,-1,-1):
    for j in range(x-1,i,-1):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
max_dp1=max(dp1)
if max_dp<max_dp1:
    max_dp=max_dp1
for i in range(x):
    if dp[i]+dp1[i]-1>max_dp:
        max_dp=dp[i]+dp1[i]-1
print(max_dp)
