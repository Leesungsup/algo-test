t=int(input())
def ans(n):
    if n <= 5:
        dp = [1, 1, 1, 2, 2]
        return dp[n-1]
    elif n > 5:
        dp = [1, 1, 1, 2, 2] + [0]*(n-5)
        for i in range(5, n):
            dp[i] = dp[i-5] + dp[i-1]
        return dp[-1]

for _ in range(t):
    print(ans(int(input())))