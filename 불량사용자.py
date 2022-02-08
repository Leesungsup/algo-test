from itertools import permutations
def check(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i])!=len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if users[i][j]=='*':
                continue
            if users[i][j]!=banned_id[i][j]:
                return False
    return True
def solution1(user_id, banned_id):
    answer=0
    ban=[]
    for users in permutations(user_id,len(banned_id)):
        if not check(users,banned_id):
            continue
        else:
            ban.append(users)
    return answer
def solution(user_id, banned_id):
    answer = 0
    arr=[]
    b={}
    n=0
    for i in banned_id:
        n+=1
        b[n]={}
        for j in user_id:
            num=0
            if len(i)==len(j):
                for k in range(len(j)):
                    if i[k]==j[k]:
                        num=0
                    elif i[k]!=j[k] and i[k]=='*':
                        num=0
                    else:
                        num=1
                        break
                if num==0:
                    if j not in b[n]:
                        b[n][j]=1
                    #arr.append(j)
        for j in b[n]:
            user_id.remove(j)
    print(arr)
    print(b)
    c={}
    n1=0
    for i in range(1,n+1):
        c[i]=[]
        print(b[i])
        for j in b[i]:
            print(j)
            if b[i][j]==1:
                b[i][j]=0
                c[i].append(j)
                for k in range(1,n+1):
                    if j in b[k] and b[k][j]==1:
                        b[k][j]=0
    print(c)
    return answer
solution1(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])
