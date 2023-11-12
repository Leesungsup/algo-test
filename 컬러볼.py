n=int(input())
lst=[]*n
answer=[0 for _ in range(n)]
for i in range(n):
    color,size=map(int,input().split())
    lst.append([size,color,i])
lst.sort()
# print(lst)
color_sum=[0 for _ in range(n)]
total=0
j=0
for i in range(n):
    while lst[j][0]<lst[i][0]:
        total+=lst[j][0]
        color_sum[lst[j][1]-1]+=lst[j][0]
        j+=1
    answer[lst[i][2]]=total-color_sum[lst[i][1]-1]
for i in range(n):
    print(answer[i])

