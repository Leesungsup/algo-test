from collections import deque
def solution(s):
    answer=0
    print(1,len(s))
    d=0
    st=[]
    min=int(1e9)
    for k in range(1,len(s)+1):
        st=[]
        b = deque([s[i : i + k] for i in range(0,len(s),k)])
        while b:
            j=b.popleft()
            for c in b:
                if c==j:
                    d+=1
                else:
                    break
            for i in range(d):
                b.popleft()
            if d==0:
                st.append(j)
            else:
                st.append(str(d+1))
                st.append(j)
                d=0
        g=''.join(st)
        if min>len(g):
            min=len(g)
    answer=min
    return answer
solution("aabbaccc")
