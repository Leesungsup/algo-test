from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons,len(dungeons)):
        now=k
        num=0
        for j in range(len(i)):
            if i[j][0]<=now:
                now-=i[j][1]
                num+=1
        if answer<num:
            answer=num
        if answer==len(i):
            #print(answer)
            return answer
    #print(answer)
    return answer