import sys
input=sys.stdin.readline
n=int(input())
road=list(map(int,input().split()))
city=list(map(int,input().split()))
road.reverse()
dp=[0]*(n)
k=[]
for i in range(n-1):
    # print(i)
    dp[i+1]=dp[i]+road[i]
    k.append((city[i],i))
k.sort(key=lambda x:x[0])
dp.reverse()
# print(dp)
s=0
answer=0
# print(k)
for i in range(n-1):
    if dp[k[i][1]]-s>0:
        # print(k[i][1])
        answer+=k[i][0]*(dp[k[i][1]]-s)
        s+=(dp[k[i][1]]-s)
print(answer)