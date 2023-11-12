import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
part=sum(arr[:m])
result=[part]
for i in range(0,n-m):
    part=part-arr[i]+arr[i+m]
    result.append(part)
print(max(result))
