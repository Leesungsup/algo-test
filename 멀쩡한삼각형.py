def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def solution(w,h):
    answer=1
    d=gcd(w,h)
    r=w+h-d
    answer=w*h-r
    return answer