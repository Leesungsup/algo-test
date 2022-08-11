for test_case in range(1,11):
    answer=0
    n=int(input())
    arr=list(input())
    stack=[]
    temp=[]
    for i in arr:
        if i=='*':
            while stack and stack[-1]=='*':
                temp.append(stack.pop())
            stack.append(i)
        elif i=='+':
            while stack:
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
            stack.append(i)
    answer=stack.pop()
    print("#{} {}".format(test_case,answer))