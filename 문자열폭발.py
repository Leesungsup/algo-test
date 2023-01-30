s=input()
b=input()
stack=[]
for i in s:
    stack.append(i)
    if i==stack[-1] and ''.join(stack[-len(b):])==b:
        del stack[-len(b):]
ans=''.join(stack[:])
if ans=='':
    print("FRULA")
else:
    print(ans)