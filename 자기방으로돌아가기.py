T=int(input())
for i in range(1,T+1):
    n = int(input())
    arr=[]
    for j in range(n):
        arr.append(list(map(int,input().split())))
    # 0~200번까지 복도 만들기
    corridor = [0] * 201
    for room in arr:
        if room[0] < room[1]:
            s = (room[0] + 1) // 2
            e = (room[1] + 1) // 2
        else:
            e = (room[0] + 1) // 2
            s = (room[1] + 1) // 2
        for j in range(s, e+1):
            corridor[j] += 1

    ans = max(corridor)
    print("#{} {}".format(i, ans))

T=int(input())
for i in range(1,T+1):
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(list(map(int,input().split())))
    print(arr)
    num=n
    arr.sort(key = lambda x:x[0])
    c=1
    for j in range(n):
        for k in range(j+1,n):
            if ((arr[k][0]<=arr[j][0]<=arr[k][1])==False or (arr[k][1]<=arr[j][0]<=arr[k][0])==False) and ((arr[j][0]<=arr[k][0]<=arr[j][1])==False or (arr[j][1]<=arr[k][0]<=arr[j][0])==False):
                if ((arr[k][0]<=arr[j][1]<=arr[k][1])==False or  (arr[k][1]<=arr[j][1]<=arr[k][0])==False) and ((arr[j][0]<=arr[k][1]<=arr[j][1])==False or (arr[j][1]<=arr[k][1]<=arr[j][0])==False):
                    continue
                else:
                    c+=1
                    break
            else:
                c+=1
                break
    print("#{} {}".format(i,c))
