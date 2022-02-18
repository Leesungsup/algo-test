def solution(s):
    answer=2
    if 0<=len(s)<=2:
        return len(s)
    left=s[0]
    right=s[-1]
    for i in range(1,len(s)-1):
        if left>s[i]:
            answer+=1
            left=s[i]
        if right>s[-1-i]:
            answer+=1
            right=s[-1-i]
    if left==right:
        answer-=1
    return answer