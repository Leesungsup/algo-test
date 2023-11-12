d=[]
while True:
    arr=[]
    s=list(input())
    if s[0]=='.':
        break
    for i in range(len(s)):
        k=s[i]
        if k=='(':
            arr.append(k)
        elif k=='[':
            arr.append(k)
        elif k==')':
            if len(arr)!=0 and arr[-1]=='(':
                arr.pop()
            else:
                arr.append(')')
                break
        elif k==']':
            if len(arr)!=0 and arr[-1]=='[':
                arr.pop()
            else:
                arr.append(']')
                break
    if len(arr)==0:
        d.append('yes')
    else:
        d.append('no')
for i in d:
    print(i)