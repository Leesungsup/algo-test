n = int(input())
arr=[[0]*n for _ in range(n)]
arr1=[[0]*n for _ in range(n)]
k=1
for i in range(n):
    for j in range(n):
        arr[i][j]=k
        k+=1
k=1
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        arr1[i][j]=k
        k+=1
for i in range(n):
    print(arr1[i])
print("------------------")

for i in range(n-1,n-n//4-1,-1):
    for j in range(n-n//4-1,n//4-1,-1):
        arr[i][j]=arr1[i][j]

for i in range(n-n//4-1,n//4-1,-1):
    for j in range(n-1,n-n//4-1,-1):
        arr[i][j]=arr1[i][j]

for i in range(n//4):
    for j in range(n-n//4-1,n//4-1,-1):
        arr[i][j]=arr1[i][j]

for i in range(n-n//4-1,n//4-1,-1):
    for j in range(n//4):
        arr[i][j]=arr1[i][j]

for i in range(n):
    print(arr[i])
