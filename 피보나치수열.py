def fibonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)
def solution(n):
    answer = 0
    print(fibonachi(n))
    return fibonachi(n)%1234567
solution(5)
def solution1(n):
    fibo=[0,1,1]
    for i in range(3,n+1):
        fibo.append((fibo[i-2]+fibo[i-1])%1234567)
    return fibo[-1]
solution1(5)
