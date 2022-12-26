n=int(input())
arr=[0]
d=[]
start=1
o=1
for i in range(n):
    c=int(input())
    k=0
    while c!=k:
        if c == arr[-1]:
            # while c!=arr[-1]:
            #     arr.pop()
            #     d.append('-')
            k=arr.pop()
            d.append('-')
        else:
            if start>c:
                o=-1
                break
            for i in range(start,c+1):
                arr.append(i)
                d.append('+')
            start=c+1

    if o==-1:
        break
if o==-1:
    print("NO")
else:
    for i in d:
        print(i)