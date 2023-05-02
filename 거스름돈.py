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

def solution2():
    count=0
    count1=0
    answer=987654321
    c=int(input())
    n=c
    count+=n//5
    n=n-5*(n//5)
    count+=n//2
    n=n-2*(n//2)
    if n==0:
        answer=count
    else:
        k=1
    n=c
    count1+=n//2
    n=n-2*(n//2)
    if n==0:
        if answer>count1:
            answer=count1
    print(answer)
solution2()
def sol(money):
    cnt = 0

    while money > 0:
        if money % 5 == 0:
            cnt += money//5
            break
        else:
            money -= 2
            cnt += 1

    if money < 0:
        print(-1)
    else:
        print(cnt)


if __name__ == '__main__':
    money = int(input())

    sol(money)