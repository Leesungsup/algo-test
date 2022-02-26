x = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(x)]
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
max_dp = max(dp)
print(max_dp)
max_idx = dp.index(max_dp)
lis = []
while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1
lis.reverse()
print(*lis)

import bisect
x = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
print(len(dp))

from bisect import bisect_left
N = int(input())
arr = [0] + list(map(int,input().split())) # input
d = [0] * (N+1) # for memoization
cmp = [-1000000001] # 이진탐색을 위해 생성.
maxVal = 0 #최대값을 저장할 변수
for i in range(1, N+1): #arr 반복 실행.
    if cmp[-1] < arr[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
        cmp.append(arr[i])
        d[i] = len(cmp) - 1
        maxVal = d[i]
    else:
        d[i] = bisect_left(cmp, arr[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
        cmp[d[i]] = arr[i] #cmp 업데이트.
print(maxVal) #최대 길이 출력
res = []
for i in range(N, 0, -1):
    if d[i] == maxVal:
        res.append(arr[i])
        maxVal -= 1
res.reverse()
print(*res)
