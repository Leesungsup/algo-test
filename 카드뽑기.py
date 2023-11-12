nums = input()
dp = [0]*(len(nums))

dp[0] = 1
if len(nums)>=2:
    if nums[1]!='0' and nums[0]+nums[1] <= '34':
        dp[1] = 2
    else:
        dp[1] = dp[0]

if len(nums)>=3:
    for i in range(2, len(nums)):
        if nums[i-1]!='0' and nums[i]!='0' and nums[i-1]+nums[i] <= '34':
            dp[i] = dp[i-1]+dp[i-2]
        elif nums[i] != '0':
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-2]
print(dp[len(nums)-1])