for test_case in range(1,11):
    n=int(input())
    arr=list(input())
    stack=[]
    check=0
    for i in range(n):
        print(stack)
        if arr[i]==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                break
        elif arr[i]==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                break
        elif arr[i]=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                break
        elif arr[i]=='>':
            if stack[-1]=='<':
                stack.pop()
            else:
                break
        else:
            stack.append(arr[i])
    if len(stack)==0:
        check=1
    else:
        check=0
    print("#{} {}".format(test_case,check))
from collections import deque
exp = {'[':']', '{':'}', '(':')', '<':'>'}
for tc in range(1, 11):
    answer = 1
    _ = int(input())
    q = deque()
    gwal = input()
    for g in gwal:
        if g in exp.keys():
            q.append(g)
        else :
            if exp[q[-1]] == g :
                q.pop()
            else:
                answer = 0
                break
    print('#{} {}'.format(tc, answer))
