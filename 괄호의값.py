import sys

arr=[]
s=list(input())
a=0
sum=0
for i in range(len(s)):
    if s[i]==')':
        a=0
        if len(arr)==0:
            print(0)
            sys.exit(0)
        while len(arr)!=0:
            x=arr.pop()
            if x=='[':
                print(0)
                sys.exit(0)
            elif x=='(':
                if a==0:
                    arr.append(2)
                else:
                    arr.append(a*2)
                break
            else:
                a+=x
    elif s[i]==']':
        a=0
        if len(arr)==0:
            print(0)
            sys.exit(0)
        while len(arr)!=0:
            x=arr.pop()
            if x=='(':
                print(0)
                sys.exit(0)
            elif x=='[':
                if a==0:
                    arr.append(3)
                else:
                    arr.append(a*3)
                break
            else:
                a+=x
    elif s[i]=='(' or s[i]=='[':
        arr.append(s[i])
    else:
        print(0)
        sys.exit(0)
answer=0
for i in arr:
    if i=='(' or i=='[':
        print(0)
        sys.exit(0)
    else:
        answer+=i
print(answer)

# arr=[]
# s=list(input())
# a=1
# sum=0
# for i in range(len(s)):
#     if s[i]=='(':
#         a*=2
#         arr.append('(')
#     elif s[i]=='[':
#         a*=3
#         arr.append('[')
#     elif s[i]==')':
#         if arr[-1]=='(':
#             sum+=a
#         else:
#             sum=0
#             break
#         a//=2
#         arr.pop()
#     elif s[i]==']':
#         if arr[-1]=='[':
#             sum+=a
#         else:
#             sum=0
#             break
#         a//=3
#         arr.pop()
# if len(arr)!=0:
#     print(0)
# else:
#     print(sum)