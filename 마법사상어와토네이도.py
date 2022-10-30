n=int(input())
a=[]
b=[[0]*n for _ in range(n)]
print(b)
for i in range(n):
    a.append(list(map(int,input().split())))
print(a)
sw=-1
w=1
h=1
count=1
c=int((n-1)/2)
r=int((n-1)/2)
while True:
    for i in range(w):
        print(c,r)
        b[c][r]=count
        r+=sw
        count+=1
    if count> n*n:
        break
    sw*=-1
    for i in range(h):
        b[c][r]=count
        c+=sw
        count+=1
    w+=1
    h+=1
for i in range(n):
    print(b[i])
