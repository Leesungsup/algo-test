def solution(s):
    answer = True
    num=0
    s1=[]
    s1=list(s)
    print(s1)
    while s1:
        a=s1.pop(0)
        print(a)
        print(num)
        if a=='(':
            num+=1
        elif a==')':
            if num==0:
                answer=False
                break
            else:
                num-=1
    print(answer)
    if num!=0:
        answer=False
    print(answer)
    return answer
solution("(())()")
def solution(s):
    answer = True
    num=0
    #s1=[]
    #s1=list(s)
    #print(s1)
    for i in range(len(s)):
        #a=s1.pop(0)
        #print(a)
        if s[i]=='(':
            num+=1
        elif s[i]==')':
            if num==0:
                return False
            else:
                num-=1
    if num!=0:
        answer=False
    #print(answer)
    return answer
