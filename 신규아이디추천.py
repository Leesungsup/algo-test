import re
def solution(new_id):
    answer=''
    if len(new_id)==0:
        new_id+='a'
    new_id=new_id.lower()
    table = str.maketrans("~!@#$%^&*()=+[{]}:?,<>/","                       ")
    new_id = new_id.translate(table)
    new_id = "".join(new_id.split())
    while True:
        if new_id.find('..') !=-1:
            new_id=new_id.replace('..','.')
        else:
            break
    while new_id[0]=='.' or new_id[-1]=='.':
        new_id=new_id.strip('.')
        if len(new_id)==0:
            new_id+='a'
    if len(new_id)>15:
        new_id=new_id[:15]
    while len(new_id)<=2:
        new_id=new_id[-1]
    answer=new_id
    return new_id
    """for a in re.finditer('.',new_id):
        if new_id[a.start()]==new_id[a.start()+1]:
            new_id=new_id.replace(new_id
            if a.start()==0 or a.start()==len(new_id):
                new_id.remove(a.start())
            if len(new_id)==0:
                new_id='a'
            if len(new_id)>15:
                new_id=new_id[:15]
            if new_id[14]=='.':
                new_id.remove(14)
    return answer"""
k='dafkdasf'
print(k.remove('d'))
k.append('a')
print(k)
k.append('a')
print(k)
