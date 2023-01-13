n = int(input())
w = []
w_b = []
dp = [1 for i in range(n)]
for i in range(n):
    w.append(list(map(int, input().split())))
w.sort(key = lambda x:x[0])
for i in range(n):
    for j in range(i):
        if w[i][1] > w[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))