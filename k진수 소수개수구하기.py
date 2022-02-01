import math
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]
def solution(n, k):
    answer = 0
    n=convert_notation(n,k)
    k=n.split('0')
    print(k)
    for i in k:
        num=0
        if i=='':
            continue
        if int(i)==1:
            continue
        for j in range(2,int(math.sqrt(int(i)))+1):
            if int(i)%j==0:
                num=1
        if num==0:
            answer+=1
    print(answer)
    return answer
solution(110011,10)
