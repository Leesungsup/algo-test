import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]
def solution(s):
    answer = [0,0]
    num=0
    while s!='1':
        print('s : '+s)
        num+=1
        n=s.count('0')
        answer[1]+=n
        print(n)
        s=convert(len(s)-n,2)
    print(s)
    answer[0]+=num
    print(answer)
    return answer
solution("110010101001")
