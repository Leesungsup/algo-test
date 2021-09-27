def solution(numbers):
    array=[]
    array=sorted(numbers)
    h=len(array)
    while True:
        num=0
        for i in array:
            if h<=i:
                num+=1
            if num>=h:
                return h
        h=h-1
n=[]
n=list(map(int,input().split()))
answer=solution(n)
print(answer)