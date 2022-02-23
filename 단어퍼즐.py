import sys
def solution(strs, t):
    answer = 0
    strs = set(strs) # 중복제거
    n = len(t)
    print(n)
    dp = [sys.maxsize]*(n+1)
    dp[0] = 0 # dp의 첫번째 값은 아무 의미없기 때문에 0으로 처리
    for i in range(n):
        s = i
        for j in range(1, 6):
            e = s + j
            if e > n:
                break
            string = t[s:e]
            print(s,e)
            print(string)
            print(dp)
            if string in strs:
                dp[e] = min(dp[s]+1, dp[e])

    return -1 if dp[-1] == sys.maxsize else dp[-1]
solution(["ba","na","n","a"],"banana")
