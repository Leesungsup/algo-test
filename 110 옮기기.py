def solution(s):
    answer=[]
    for str in s:
        stack=[]
        n=0
        for st in str:
            if len(stack)>=2 and stack[-1]=='1' and stack[-2]=='1' and st=='0':
                n+=1
                stack.pop()
                stack.pop()
            else:
                stack.append(st)
        count=0
        for i in stack[::-1]:
            if i=='0':
                break
            else:
                count+=1
        answer.append(''.join(stack[:len(stack)-count])+'110'*n+'1'*count)
    return answer