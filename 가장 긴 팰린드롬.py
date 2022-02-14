from collections import deque
def solution(s):
    answer = 0
    q=[]
    for i in range(len(s)-1,-1,-1):
        q.append(s[i])
    q1=q[:]
    q2=list(s)
    #print(q1)
    #print(q2)
    for i in range(len(s),0,-1):
        num=0
        for j in range(i):
            if s[j]!=q1[j]:
                num=1
        if num==0:
            a=i
            break
        else:
            q1.pop(0)
    #print(q)
    #print(q1)
    for i in range(len(q),0,-1):
        num=0
        for j in range(i):
            if q[j]!=q2[j]:
                num=1
        if num==0:
            b=i
            break
        else:
            q2.pop(0)
    #print(q2)
    #print(answer)
    if a<b:
        return b
    else:
        return a
    #return answer
#solution("abbb")
def solution1(s):
    answer=0
    l=list(s)
    for i in range(len(s)//2):
        num=0
        print(i)
        for j in range(len(l)//2-i):
            if l[i]!=l[len(l)-i-1]:
                num=1
        if num==0:
            answer=len(s)-i*2
    print(answer)
solution1("abbb")
def isPalindrome(s):
    if s==s[::-1]:
        return True
def solution2(s):
    answer=-1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if answer<len(s[i:j]):
                    answer=len(s[i:j])
    print(answer)
    return answer
solution2("abbb")
