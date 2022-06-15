from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    sum=0
    prices=list(map(int,input().split()))
    for i in range(n):
        if len(prices)==0:
            break
        k=prices.pop()
        c=0
        for j in range(len(prices)-1,-1,-1):
            if k>prices[j]:
                c+=1
                sum+=k-prices[j]
            else:
                break
        for m in range(c):
            prices.pop()
    print("#{} {}".format(test_case,sum))
    # ///////////////////////////////////////////////////////////////////////////////////
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=input()
    prices=list(map(int,input().split()))
    q=deque(prices)
    before=0
    b=deque()
    sum=0
    while q:
        k=q.popleft()
        if len(b)==0:
            b.append(k)
        elif b[-1]>k:
            for i in b:
                sum+=b[-1]-i
            while b:
                b.popleft()
            b.append(k)
        else:
            b.append(k)
            if len(q)==0:
                for i in b:
                    sum+=b[-1]-i
    print("#{} {}".format(test_case,sum))
    # ///////////////////////////////////////////////////////////////////////////////////
