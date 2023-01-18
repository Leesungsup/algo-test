n,k=map(int,input().split())
arr=[]
count=0
for i in range(n):
    arr.append(int(input()))
for i in range(n-1,-1,-1):
    if k==0:
        break
    if k//arr[i]!=0:
        count+=k//arr[i]
        k=k%arr[i]
print(count)