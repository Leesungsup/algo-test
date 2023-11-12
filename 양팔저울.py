import sys
input=sys.stdin.readline
n=int(input())
arr1=list(map(int,input().split()))
k=int(input())
arr2=list(map(int,input().split()))
dp=[[0]*(30*500+1) for _ in range(n+1)]
result=set()
def get_result(pends, n, now, left, right):
    """
    pends : 추 목록
    n : 전체 추의 개수
    now : 이제 놓을 추의 index
    left : 왼쪽 팔의 무게
    right : 오른쪽 팔의 무게
    """
    new = abs(left - right)


    if new not in result:
        result.add(new)

    if now == n :
        return 0

    if dp[now][new] == 0:
        get_result(pends, n, now+1, left + pends[now], right)
        get_result(pends, n, now+1, left, right + pends[now])
        get_result(pends, n, now+1, left, right)
        dp[now][new] = 1
def knapsack(W,wt,val,n):
    K=[[0]*(W+1) for _ in range(n+1)]
    for i in range(n):
        for w in range(W):
            if i==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
get_result(arr1,n,0,0,0)
for i in arr2:
    if i in result:
        print('Y',end=' ')
    else:
        print('N',end=' ')