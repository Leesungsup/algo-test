def solution(s):
    answer = -1
    stack=[]
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        answer=0
    else:
        answer=1
    s2=''
    for i in range(len(s)):
        if s2==s:
            break
        s2=s
        s = s.replace("aa","")
        s = s.replace("bb","")
        s = s.replace("cc","")
        s = s.replace("dd","")
        s = s.replace("ee","")
        s = s.replace("ff","")
        s = s.replace("gg","")
        s = s.replace("hh","")
        s = s.replace("ii","")
        s = s.replace("jj","")
        s = s.replace("kk","")
        s = s.replace("ll","")
        s = s.replace("mm","")
        s = s.replace("nn","")
        s = s.replace("oo","")
        s = s.replace("pp","")
        s = s.replace("qq","")
        s = s.replace("rr","")
        s = s.replace("ss","")
        s = s.replace("tt","")
        s = s.replace("uu","")
        s = s.replace("vv","")
        s = s.replace("ww","")
        s = s.replace("xx","")
        s = s.replace("yy","")
        s = s.replace("zz","")
    """while True:
        if s==s2:
            break
        s2=s
        s1=[s[i:i+1] for i in range(0,len(s),1) if len(s[i:i+1])==1]
        for i in range(len(s1)-1):
            if s1[i]==s1[i+1]:
                s1[i]=''
                s1[i+1]=''
        s=''.join(s1)"""
    if s=='':
        answer=1
    else:
        answer=0
    print(answer)
    return answer
solution('baabaa')
def solution1(s):
    answer=0
    st=list(s)
    q=[]
    for i in st:
        if len(q)==0:
            q.append(i)
        else:
            if q[-1]==i:
                q.pop(-1)
            else:
                q.append(i)
    return 1 if len(q)==0 else 0
    if len(q)==0:
        return 1
    else :
        return 0
print(solution1('baabaa'))