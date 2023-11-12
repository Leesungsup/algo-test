import sys
input=sys.stdin.readline
n,k=map(int,input().split())
def factorial(n):
    ans=1
    for i in range(2,n+1):
        ans*=i
    return ans
def bino_coef_factorial(n,r):
    return factorial(n)//factorial(r)//factorial(n-r)
print(bino_coef_factorial(n,k))

def bino_coef(n,k):
    if k==0 or n==k:
        return 1
    return bino_coef(n-1,k)+bino_coef(n-1,k-1)
print(bino_coef(5,2))

def bino_coef1(n,k):
    cache=[[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        cache[i][0]=1
    for i in range(k+1):
        cache[i][i]=1
    for i in range(1,n+1):
        for j in range(1,k+1):
            cache[i][j]=cache[i-1][j]+cache[i-1][j-1]
    return cache[n][k]

def bino_coef2(n,k):
    if k>n:
        return 0
    cache=[[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times,got):
        if times==n:
            return got==k
        if cache[times][got]!=-1:
            return cache[times][got]
        cache[times][got]=choose(times+1,got)+choose(times+1,got+1)
        return cache[times][got]
    return choose(0,0)
print(bino_coef2(n,k))


#모듈러 법칙 {a = b(mod c)} == {a(mod c) = b(mod c)}
#페르마의 소정리 a**(p-1) = 1(mod p)
# a=**(p-1) = a*a**(p-2) = 1(mod p) = a**(p-2)=a**(-1) (mod p)
#p는 소수 a는 p의 서로소(1이외에 겹치는 약수가 없는 것)
def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007
N, K = map(int, input().split())

fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = (fact[N - K] * fact[K]) % p

print((A % p) * (power(B, p - 2) % p) % p)