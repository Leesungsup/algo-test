d=[]
arr=[]
n=int(input())
for i in range(n):
    s=input()
    if 'push' in s.split():
        arr.append(s.split()[1])
    elif 'pop' in s.split():
        if len(arr)==0:
            d.append(-1)
        else:
            d.append(arr.pop())
    elif 'top' in s.split():
        if len(arr)==0:
            d.append(-1)
        else:
            d.append(arr[-1])
    elif 'empty' in s.split():
        if len(arr)==0:
            d.append(1)
        else:
            d.append(0)
    elif 'size' in s.split():
        d.append(len(arr))
for i in d:
    print(i)