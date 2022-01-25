def solution(n):
    answer = 0
    arr=[]
    for i in range(1,n+1):
        arr.append(i)
    print(arr)
    k=0
    while True:
        num=0
        for i in range(k,n):
            num+=arr[i]
            if num==n:
                answer+=1
                break
            elif num>n:
                break
        if k==n:
            break
        k+=1
    print(answer)
    return answer
solution(15)
