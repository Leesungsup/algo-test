def solution(n,a,b):
    answer = 0
    time=0
    while True:
        time+=1
        if (a+1)==b:
            break
        if a%2==0:
            a=a//2
        elif a%2!=0:
            a=(a//2)+(a%2)
        if b%2==0:
            b=b//2
        elif b%2!=0:
            b=(b//2)+(b%2)


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(time)

    return answer
solution(8,4,7)
def solution(n,a,b):
    answer = 0
    time=0
    while True:
        time+=1
        if a==b:
            break
        elif (b+1)==a:
            break
        a=(a//2)+(a%2)
        b=(b//2)+(b%2)
    answer=time
    return answer
def solution(n,a,b):
    answer = 0
    time=0
    while True:
        time+=1
        if a==b:
            break
        a=(a//2)+(a%2)
        b=(b//2)+(b%2)
    answer=time-1
    return answer