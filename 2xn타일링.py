def factorial(n) :
    answer = 1
    for i in range(2, n + 1) :
        answer *= i
    return answer
def solution(n) :
    answer = 0
    if n < 2 :
        answer = 1
    else :
        for i in range(n // 2 + 1) :
            a = (n // 2) - i
            b = (n % 2) + (2 * i)
            #print(a, b, 2*a+b)
            answer += factorial(a + b) / (factorial(a) * factorial(b))
    return answer % 1000000007

def solution(n) :
    answer = 0
    lst = [0 for i in range(n)]
    lst[0] = 1
    lst[1] = 2
    for i in range(2, n) :
        lst[i] = (lst[i - 1] + lst[i - 2]) % 1000000007
    answer = lst[n - 1]
    return answer