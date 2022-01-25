import re
def solution(s):
    answer = ''
    s=s.lower()
    #s=' '.join(s.split())
    #list=s.split()
    list=re.findall(' +\w', s)
    print(list)
    num=0
    for i in list:
        s=s.replace(i,i.upper())
    print(s)
    """for i in list:
        if i==' ':
            continue
        else:
            print(i[0].upper()+i[1:])
            list[num]=i[0].upper()+i[1:].lower()
        num+=1"""
    return ' '.join(list)
solution("3people unFollowed me")
def solution(s):
    s=s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i]=s[i][0].upper()+s[i][1:].lower()
    return ' '.join(s)
def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer
