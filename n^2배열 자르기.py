def solution(n, left, right):
    answer = []
    a=[]
    for i in range(1,n+1):
        a.append(i)
    for i in range(2,n+1):
        for j in range(i):
            a.append(i)
        for j in range(i+1,n+1):
            a.append(j)
    print(a)
    answer=a[left:right+1]
    print(answer)
    return answer
solution(3,2,5)
#1222
#123223333
#1234223433344444
#1234522345333454444555555

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n
        b = i%n
        answer.append(max(a,b)+1)
    return answer
