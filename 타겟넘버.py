from collections import deque
def solution(numbers,target):
    answer=0
    q=deque()
    q.append((0,numbers[0]))
    q.append((0,-numbers[0]))
    num=0
    k=0
    while q:
        index,num=q.popleft()
        if index+1==len(numbers):
            if num==target:
                answer+=1
        else:
            q.append((index+1,num-numbers[index+1]))
            q.append((index+1,num+numbers[index+1]))
    return answer
def solution(numbers,target):
    answer=0
    q=[]
    q=deque()
    n=len(numbers)
    q.append((-numbers[0],0))
    q.append((+numbers[1],0))
    while q:
        num,i=q.popleft()
        if n==i+1:
            if target==num:
                answer+=1
        else:
            q.append((num-numbers[i+1],i+1))
            q.append((num+numbers[i+1],i+1))
    print(answer)
numbers=list(map(int,input().split()))
target=int(input())
solution(numbers,target)
#트리를 만드는 방법에대하여 공부가 더 필요하다는 것을 깨달았습니다.