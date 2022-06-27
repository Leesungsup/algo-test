import re
T=int(input())
for i in range(1,T+1):
    arr=input()
    for j in range(1,11):
        m=re.complie(arr[:j])
        print(m.findall(arr))
case_count = int(input())
for i in range(1, case_count + 1):
    string = input()
    word = ''
    for char in string:
        word += char
        length = len(word)
        if word == string[length:length+length]:
            break
    print('#{} {}'.format(i, len(word)))
T=int(input())
for i in range(1,T+1):
    arr=input()
    ma=0
    for j in range(1,11):
        str=""
        for k in range(0,len(arr),j):
            if len(str)==0:
                str=arr[k:k+j]
            else:
                if str==arr[k:k+j]:
                    print(str)
                    ma=len(str)
                else:
                    break
        if ma!=0:
            break
    print("#{} {}".format(i,ma))
