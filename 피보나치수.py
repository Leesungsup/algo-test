ans1=0
ans2=0
def fib(n):
    global ans1
    ans1+=1
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonzcci(n):
    global ans2
    arr=[0]*(n+1)
    arr[1]=arr[2]=1
    for i in range(3,n+1):
        arr[i]=arr[i-1]+arr[i-2]
        ans2+=1
    return arr[n]
n=int(input())
# print(fib(n), fibonzcci(n))
print(fib(n), ans2)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    cnt2=0
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n=int(input())
print(fib(n),fibonacci(n))