from itertools import combinations
T=int(input())
for test_case in range(1,T+1):
    n,b=map(int,input().split())
    arr=list(map(int,input().split()))
    carr=[]
    min=987654321
    count=0
    for i in range(n+1,1,-1):
        if count >=5:
            break
        carr=combinations(arr,i)
        for j in carr:
            if sum(j)>=b:
                count=0
                if min>b-sum(j):
                    min=b-sum(j)
            else:
                count+=1
    print("#{} {}".format(test_case,min))
T = int(input())

def top(idx, height):
    global min_height
    if B <= height < min_height:
        min_height = height
    if idx == N:
        return
    top(idx+1, height)
    top(idx+1, height + height_lst[idx])

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height_lst = list(map(int, input().split()))
    min_height = 200000
    top(0, 0)
    print('#{} {}'.format(test_case, min_height - B))