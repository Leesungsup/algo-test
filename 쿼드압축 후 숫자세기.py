def solution(arr):
    answer=[0,0]
    l=len(arr)
    def quard(a,b,l):
        s=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if s!=arr[i][j]:
                    l=l//2
                    quard(a,b,l)
                    quard(a+l,b,l)
                    quard(a,b+l,l)
                    quard(a+l,b+l,l)
                    return
        answer[s]+=1
    quard(0,0,l)
    return answer