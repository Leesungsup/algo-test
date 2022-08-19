import math
T=int(input())
def dfs(n,time):
    global answer
    if n==2:
        if answer>time:
            answer=time
            print(answer)
        return
    if math.sqrt(n).is_integer():
        dfs(math.sqrt(n),time+1)
    dfs(n+1,time+1)
for test_case in range(1,T+1):
    n=int(input())
    print(n)
    answer=987654321
    #dfs(n,0)
    result=0
    while n!=2:
        print(n)
        if n == 1:
            result += 1
            break
        if math.sqrt(n).is_integer():
            print(n)
            n=int(math.sqrt(n))
            result+=1
        else:
            result+=pow(int(math.sqrt(n))+1,2) - n
            n=int(math.sqrt(n))+1
            result+=1
    print("#{} {}".format(test_case,int(result)))
