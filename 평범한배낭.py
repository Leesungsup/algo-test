n,k=map(int,input().split())
m=[[0]*(k+1) for _ in range(n)]
item=[]
for i in range(n):
    item.append(list(map(int,input().split())))
#냅색 문제 풀이
for i in range(n):
    for j in range(1, k + 1):
        w = item[i][0]
        v = item[i][1]
        if j < w:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(v + m[i - 1][j - w], m[i - 1][j])
print(m[n-1][k])