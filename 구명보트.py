def solution(people,limit):
    answer=0
    people.sort()
    while people:
        if len(people)==1:
            answer+=1
            break
        if people[0]+people[-1]<=limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
        answer+=1
    return answer
def solution1(people,limit):
    answer=0
    a=0
    b=len(people)-1
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1
            answer+=1
        b-=1
    return len(people)-answer
def solution2(people,limit):
    answer=0
    people.sort()
    i=0
    j=len(people)-1
    while i<=j:
        answer+=1
        if people[i]+people[j]<=limit:
            i+=1
        j-=1
    return answer