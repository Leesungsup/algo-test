
def ans(n):
    if n <= 2:
        dp = [1, 2]
        return dp[n-1]
    elif n > 2:
        dp = [1, 2] + [0]*(n-2)
        for i in range(2, n):
            dp[i] = dp[i-2]%15746 + dp[i-1]%15746
        return dp[-1]


print(ans(int(input()))%15746)