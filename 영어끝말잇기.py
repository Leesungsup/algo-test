def solution(n, words):
    answer = []
    a={}
    num=0
    number=1
    c=0
    a[words[0]]=1
    for i in range(1,len(words)):
        num+=1
        num=num%n
        if len(a)%n==0:
            number+=1
        #print(num)
        print(a)
        if words[i][0]!=words[i-1][-1]:
            #print("걸린사람 : ",num+1)
            answer.append(num+1)
            c=1
            break
        if words[i] not in a:
            a[words[i]]=1
        elif words[i] in a:
            #print("걸린사람 : ",num+1)
            answer.append(num+1)
            c=1
            break
    if c==1:
        answer.append(number)
    elif c==0:
        return [0,0]
    print(answer)
    return answer
solution(2,["land", "dream", "mom", "mom", "ror"])
