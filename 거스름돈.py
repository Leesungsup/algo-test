def solution(n, money):
    answer = 0
    result=[]
    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(money)):
            dfs(csum - money[i], i, path + [money[i]])
    dfs(n, 0, [])
    print(result)
    return len(result)
solution(5,[1,2,5])
def solution1(n,money):
    answer=0
    dp=[0 for _ in range(n+1)]
    print(dp)
    dp[0]=1
    for i in money:
        for j in range(1,n+1):
            if j>=i:
                dp[j]+=dp[j-i]
    print(dp)
    return answer
solution1(5,[1,2,5])
