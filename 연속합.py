import sys
input = sys.stdin.readline
max=-987654321
K = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0]*(K+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, K+1):
        if j==i+1:
            dp[i][j] = arr[i] + arr[j]

for i in range(K-1, 0, -1):
    for j in range(1, K+1):
        if dp[i][j] == 0 and j>i:
            dp[i][j] = max([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(arr[i:j+1])
            if dp[i][j]>max:
                max=dp[i][j]
print(max)

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))