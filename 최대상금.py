T=int(input())
def dfs(count):
    global answer
    if not count:
        temp = int(''.join(values))
        if answer < temp:
            answer = temp
        return
    for i in range(length):
        for j in range(i+1, length):
            values[i], values[j] = values[j], values[i]
            temp_key = ''.join(values)
            if visited.get((temp_key, count-1), 1):
                visited[(temp_key, count-1)] = 0
                dfs(count-1)
            values[i], values[j] = values[j], values[i]
for test_case in range(1,T+1):
    answer = 0
    value, change = input().split()
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}
    dfs(change)
    print('#{} {}'.format(test_case, answer))

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
