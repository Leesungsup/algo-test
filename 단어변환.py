def dfs(begin,target,words,visited):
    num=0
    stack=[begin]
    while stack:
        s=stack.pop()
        if s==target:
            return num
        for w in range(0,len(words)):
            if len([i for i in range(0,len(s)) if words[w][i]!=s[i]])==1:
                if visited[w]==1:
                    continue
                visited[w]=1
                stack.append(words[w])
        num+=1
def solution(begin,target,words):
    answer=0
    visited=[0 for i in range(0,len(words))]
    if target not in words:
        answer=0
    else:
        answer=dfs(begin,target,words,visited)
    return answer
