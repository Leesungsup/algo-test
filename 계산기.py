for test_case in range(10):
    N = int(input())
    s = input()
    tokens = []
    stack = []
    result = []
    for i in range(N):
        if s[i].isdigit():
            tokens.append(int(s[i]))
        else:
            if s[i] == ')':
                chk = ''
                while chk != '(':
                    chk = stack.pop()
                    tokens.append(chk)
                tokens.pop()
                continue
            elif s[i] == '*':
                while stack and stack[-1] == '*' and stack[-1] != "(":
                    tokens.append(stack.pop())
            elif s[i] == '+':
                while stack and stack[-1] != "(":
                    tokens.append(stack.pop())
            stack.append(s[i])

    while stack:
        tokens.append(stack.pop())

    for i in tokens:
        if i in range(0, 10):
            result.append(i)
        else:
            if i == "+":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 + p1)
            elif i == "*":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 * p1)

    print("#{} {}".format(test_case,result[-1]))

for test_case in range(1,11):
    answer=0
    n=int(input())
    arr=list(input())
    stack=[]
    temp=[]
    for i in arr:
        if i==')':
            chk=''
            if chk=='(':
                chk=stack.pop()
                temp.append(chk)
            temp.pop()
            continue
        if i=='*':
            while stack and stack[-1]=='*' and stack[-1]!='(':
                temp.append(stack.pop())
            stack.append(i)
        elif i=='+':
            while stack and stack[-1]!='(':
                temp.append(stack.pop())
            stack.append(i)
        elif i.isdigit():
            temp.append(i)
    while stack:
        temp.append(stack.pop())
    for i in temp:
        if i in "*+":
            b=stack.pop()
            a=stack.pop()
            if i=='*':
                stack.append(a*b)
            else:
                stack.append(a+b)
        else:
            stack.append(int(i))
    answer=stack.pop()
    print("#{} {}".format(test_case,answer))