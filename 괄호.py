d=[]
n=int(input())
for i in range(n):
    arr=[]
    s=list(input())
    for i in range(len(s)):
        k=s[i]
        if k=='(':
            arr.append(k)
        else:
            if len(arr)!=0:
                arr.pop()
            else:
                arr.append(')')
                break
    if len(arr)==0:
        d.append('YES')
    else:
        d.append('NO')
for i in d:
    print(i)