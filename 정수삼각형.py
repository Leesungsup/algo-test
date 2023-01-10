n=int(input())
arr=[[] for _ in range(n)]
# arr1=[[0]*i for i in range(1,n+1)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
# print(arr)
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            arr[i][j]=arr[i][j]+arr[i-1][j]
        elif j==i:
            arr[i][j]=arr[i][j]+arr[i-1][j-1]
        else:
            arr[i][j]=max(arr[i-1][j]+arr[i][j],arr[i-1][j-1]+arr[i][j])
print(max(arr[-1]))

