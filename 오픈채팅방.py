from collections import defaultdict
def solution1(record):
    answer = []
    a=[]
    k=defaultdict()
    for i in record:
        a=i.split()
        if a[0]=="Enter":
            k[a[1]]=a[2]
        elif a[0]=="Change":
            k[a[1]]=a[2]
    for i in record:
        a=i.split()
        if a[0]=="Enter":
            answer.append(k[a[1]]+"님이 들어왔습니다.")
        elif a[0]=="Leave":
            answer.append(k[a[1]]+"님이 나갔습니다.")
    return answer