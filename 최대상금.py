def dfs(n,count):
    global result
    if count==int(cnt):
        if result<int(''.join(data)):
            result=int(''.join(data))
    for i in range(len(data)):
        for j in range(i,len(data)):
            if data[i]<data[j]:
                data[i],data[j]=data[j],data[i]
                dfs(i,count+1)
                data[i],data[j]=data[j],data[i]
    if result == 0 and count < int(cnt) :
        extra = (int(cnt) - count) % 2
        if extra == 1:
            data[-1], data[-2] = data[-2], data[-1]
        dfs(n, int(cnt))
T=int(input())
for i in range(1,T+1):
    data, cnt = input().split()
    data = list(data)
    result=0
    dfs(0,0)
