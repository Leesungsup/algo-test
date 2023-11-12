def solution(n):
    answer=[]
    def move(n,start,to):
        answer.append([start,to])
    def hanoi(n,start,to,via):
        if n==1:
            move(1,start,to)
        hanoi(n-1,start,via,to)
        move(n,start,to)
        hanoi(n-1,via,to,start)
    hanoi(n,1,3,2)
    return answer
solution(3)

def solution(n):
    answer=[]
    def move(n,start,to):
        answer.append([start,to])
    def hanoi(n,start,to,via):
        if n==1:
            move(1,start,to)
        hanoi(n-1,start,via,to)
        move(n,start,to)
        hanoi(n-1,via,to,start)