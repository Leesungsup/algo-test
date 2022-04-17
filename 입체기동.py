n=int(input())
a=[]
for i in range(n):
    s,k=map(int,input().split())
    a[i].append((s,k))
a.sort(key=lambda x:x[0])
print(a)