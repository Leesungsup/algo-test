def binary(l,target,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if l[mid]==target:
        return cnt.get(target)
    elif l[mid]>target:
        return binary(l,target,start,mid-1)
    else:
        return binary(l,target,mid+1,end)
n=int(input())
a=sorted(list(map(int,input().split())))
m=int(input())
b=list(map(int,input().split()))
cnt={}
for i in a:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
for i in b:
    print(binary(a,i,0,len(a)-1),end=' ')