import sys
read = sys.stdin.readline

n = int(read())
arr =[list(map(int, read().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
print(arr)
print(min(arr[-1]))


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