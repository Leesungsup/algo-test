from itertools import combinations
def f1(x):
    return my_dict[x]
def solution(orders, course):
    my_dict = {'x':10, 'y':30, 'z': 20,'k':30}
    #key_max = max(my_dict.keys(), key=f1)
    key_min = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    #print('Max -',key_max,my_dict[key_max])
    print('Min -',key_min,my_dict[key_min])
    answer = []
    orde=[]
    for i in range(len(orders)):
        k=list(orders[i])
        orde.append(sorted(list(orders[i])))
    for i in course:
        d=dict()
        for j in orde:
            for k in combinations(j,i):
                if ''.join(k) not in d:
                    d[''.join(k)]=1
                else:
                    d[''.join(k)]+=1
        print(d)
        if len(d.keys())==0:
            continue
        key_max=max(d.keys(),key=(lambda k: d[k]))
        for i in list(d.keys()):
            if d[key_max]>=2 and d[key_max]==d[i]:
                answer.append(i)
    answer.sort()
    print(answer)
    return answer
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])
