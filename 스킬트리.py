def solution(skill, skill_trees):
    answer = 0
    s=list(skill)
    for i in skill_trees:
        num=0
        c=0
        for j in i:
            if j in s:
                if s[c]!=j:
                    num=1
                    break
                else:
                    c+=1
        if num==0:
            answer+=1
    print(answer)
    return answer
solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])
