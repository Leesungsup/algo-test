from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    d=defaultdict()
    k=defaultdict()
    for i in enroll:
        d[i]=''
        k[i]=0
    for i in range(len(enroll)):
        for j in range(len(referral)):
            if enroll[i]==referral[j]:
                d[enroll[j]]=enroll[i]
    #print(d)
    #print(k)
    for i in range(len(seller)):
        c=seller[i]
        k[c]+=(amount[i]*100)-((amount[i]*100)//10)
        na=(amount[i]*100)//10
        for j in range(len(enroll)):
            if d[c]!='':
                #print(c)
                #print(na)
                #print(d[c])
                k[d[c]]+=na-na//10
                na=na//10
                c=d[c]
                if d[c]=='':
                    break
            else:
                break
    #print(k)
    for i in k:
        answer.append(k[i])
    #print(answer)
    return answer

def solution(enroll, referral, seller, amount):
    tree = {'-' : 'root'}
    sell = {'-' : 0}
    for i in range(len(enroll)):
        child = enroll[i]
        parent = referral[i]
        sell[child] = 0
        tree[child] = parent

    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        money = amount[i] * 100
        sell[child] += money
        while True:
            commission = money // 10
            sell[child] -= commission
            sell[parent] += commission
            child = parent
            parent = tree[child]
            money = commission
            if parent == 'root':
                break
    ans = []
    for person in enroll:
        ans.append(sell[person])
    return ans