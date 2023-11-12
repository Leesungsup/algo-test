


def solution(s):
    s=input()
    n = len(s)
    answer = (n-1)*n*(n+1)/6
    char = {}
    cnt = 1
    first = ''
    for c in s:
        if c not in char:
            char[c] = {}
        if first == c:
            cnt += 1
            if cnt not in char[c]:
                char[c][cnt] = 1
            else:
                char[c][cnt] += 1
            char[c][cnt-1] -= 1
        else:
            cnt = 1
            if cnt not in char[c]:
                char[c][cnt] = 1
            else:
                char[c][cnt] += 1
        first = c

    for c in char:
        total = sum(l * cnt for l, cnt in char[c].items())
        val = sum(char[c].values())
        for n in char[c]:
            answer -= total*(total-1)//2
            total -= val
            val -= char[c][n]
    print(answer)
    return answer


def solution(s):
    arr=[]
    for i in range(len(s)-1):
        for j in range(len(s)):
            arr.append(s[i:j+1])
    print(arr)
    answer=0
    for i in arr:
        if len(i)<=1:
            continue
        m=-1
        for k in range(len(i)):
            if i[k]!=i[len(i)-1]:
                if m<(len(i)-1-k):
                    m=(len(i)-1-k)
                    print(k,len(i)-1,m)
        answer+=m
    print(answer)
    s=input()
    answer=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            arr=s[i:j+1]
            print(arr)
            m=0
            for k in range(len(arr)):
                if arr[k]!=arr[len(arr)-1]:
                    if m<(len(arr)-1-k):
                        m=(len(arr)-1-k)
                        print(k,len(arr)-1,m)
            answer+=m
    print(answer)
    return answer
print(solution("baby"))

def solution(s):
    answer=0
    for i in range(len(s)):
        arr1=[]
        arr2=[]
        m=0
        arr1.append(s[i])
        arr2.append(i)
        for j in range(i+1,len(s)):
            if s[j] not in arr1:
                arr1.append(s[j])
                arr2.append(j)
            elif s[j] in arr1 and arr1.index(s[j])!=0:
                arr2[arr1.index(s[j])]=j
            if len(arr2)>=2:
                for j in range(1,len(arr2)):
                    if (arr2[j]-arr2[0])>m:
                        m=(arr2[j]-arr2[0])
            answer+=m
    print(answer)
    return answer