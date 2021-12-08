def solution(s):
    answer = 0
    g=[]
    a=dict()
    a={"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    k=list(s)
    for i in range(len(s)):
        if k[i].isalpha():
            if ''.join(k[i:i+4])=='zero' or ''.join(k[i:i+4])=='four' or ''.join(k[i:i+4])=='five' or ''.join(k[i:i+4])=='nine':
                g.append(a[''.join(k[i:i+4])])
            elif ''.join(k[i:i+3])=='one' or ''.join(k[i:i+3])=='two' or ''.join(k[i:i+3])=='six':
                g.append(a[''.join(k[i:i+3])])
            elif ''.join(k[i:i+5])=='three' or ''.join(k[i:i+5])=='seven' or ''.join(k[i:i+5])=='eight':
                g.append(a[''.join(k[i:i+5])])
        else:
            g.append(k[i])
    answer=int(''.join(g))
    print(answer)
    return answer
solution("one4seveneight")
