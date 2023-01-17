import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
count=0
# for i in range(n):
#     dp[i+1]=dp[i]+arr[i]
# for i in range(0,n+1):
#     # print(i,"번째")
#     for j in range(1,n-i+1):
#         if (dp[j+i] - dp[j - 1])%m==0:
#             count+=1
#         # print(dp[j+i] - dp[j - 1])
# print(count)

for i in range(1,n+1):
    part=sum(arr[:i])
    if part%m==0:
        count+=1
    # print(i,"번째")
    for j in range(0,n-i):
        part=part-arr[j]+arr[j+i]
        # print(part)
        if part%m==0:
            count+=1
    # print()
print(count)


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split())) + [0]
r = [0] * m

for i in range(n):
    num[i] += num[i - 1]
    r[num[i] % m] += 1

cnt = r[0]

for i in r:
    cnt += i * (i - 1) // 2

print(cnt)