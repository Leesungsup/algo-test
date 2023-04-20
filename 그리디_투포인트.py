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

import bisect

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)

n,m=map(int,input().split())
count=0
max=-987654321
nums=list(map(int,input().split()))
for i in range(len(nums)-m+1):
    print(i,i+m)
    print(nums[i:i+m])
    if sum(nums[i:i+m])>max:
        max=sum(nums[i:i+m])
        count=1
    elif sum(nums[i:i+m])>max:
        count+=1
print(max)
print(count)

m=int(input())
answer=[]
nums=list(map(int,input().split()))
for i in range(len(nums)):
    for j in range(i+2,len(nums)+1):
        print(nums[i:j])
        if sum(nums[i:j])==m:
            answer.append((i+1,j+1))
        elif sum(nums[i:j])<m:
            continue
        elif sum(nums[i:j+1])>m:
            break
print(len(answer))
for i in range(len(answer)):
    print(answer[i])