def solution(n):
    ans = 0
    while n:
        if n%2==0:
            n=n//2
        elif n%2!=0:
            ans+=1
            n=n//2
        elif n==1:
            ans+=1
            break
    print(ans)
    return ans
solution(5000)
