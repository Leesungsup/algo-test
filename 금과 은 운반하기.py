def solution(a, b, g, s, w, t):
    answer = (10**5)*(10**9)*4
    end=(10**5)*(10**9)*4
    start=0
    while start<=end:
        mid=(start+end)//2
        print("mid : ",mid)
        gold=0
        silver=0
        total=0
        for i in range(0,len(g)):
            cnt=mid//(t[i]*2)
            print("cnt : ",cnt)
            if mid%(t[i]*2)>=t[i]:
                cnt+=1
            if g[i]<cnt*w[i]:
                gold+=g[i]
            else:
                gold+=cnt*w[i]
            if s[i]<cnt*w[i]:
                silver+=s[i]
            else:
                silver+=cnt*w[i]
            if s[i]+g[i]<=cnt*w[i]:
                total+=(s[i]+g[i])
            else:
                total+=cnt*w[i]
        if gold >= a and silver >= b and total >= a + b :
            end = mid - 1
            answer = min(answer, mid)
            print(answer)
        else:
            start = mid + 1
    return answer
solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
