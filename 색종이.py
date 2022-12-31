arr=[]
count=0
for i in range(6):
    arr.append(int(input()))
if arr[5]>0:
    count+=arr[5]
    arr[5]=0
if arr[4]>0:
    count+=arr[4]
    if arr[0]>0:
        if arr[0]<arr[4]*11:
            arr[0]=0
        else:
            arr[0]-=arr[4]*11
if arr[3]>0:
    count+=arr[3]
    if arr[3]*5>arr[1]:
        arr[1]=arr[1]%5
        if arr[1]>0:
            k3=5-arr[1]
            arr[1]=0
            if k3*4>arr[0]:
                arr[0]=0
            else:
                arr[0]-=k3*4
        elif arr[0]>0:
            if arr[3]*20>arr[0]:
                arr[0]=0
            else:
                arr[0]-=arr[3]*20
    else:
        arr[1]=arr[1]-arr[3]*5
if arr[2]>0:
    count+=arr[2]//4
    k=0
    if arr[2]%4>0:
        count+=1
        arr[2]=arr[2]%4
        k=4-arr[2]
        arr[2]=0
    if arr[1]>0 and k>0:
        if arr[1]<k*2-1:
            arr[1]=0
            if k==3:
                if arr[0]<7:
                    arr[0]=0
                else:
                    arr[0]-=7
            if k==2:
                if arr[0]<6:
                    arr[0]=0
                else:
                    arr[0]-=6
            if k==1:
                if arr[0]<5:
                    arr[0]=0
                else:
                    arr[0]-=5
        else:
            arr[1]-=k*2-1
    elif arr[0]>0 and k>0:
        if arr[0]<k*9:
            arr[0]=0
        else:
            arr[0]-=k*9

if arr[1]>0:
    count+=arr[1]//9
    k=0
    if arr[1]%9>0:
        count+=1
        arr[1]=arr[1]%9
        k=9-arr[1]
    if arr[0]>0 and k>0:
        if arr[0]<k*4:
            arr[0]=0
        else:
            arr[0]-=k*4
if arr[0]>0:
    count+=arr[0]//36
    arr[0]=arr[0]%36
    if arr[0]>0:
        count+=1
print(count)

paper = [0]
ans = 0
for _ in range(6):
    paper.append(int(input()))

if paper[6]:
    ans += paper[6]

while paper[5]:
    area = 36 - 5*5
    paper[5] -= 1
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[4]:
    area = 36 - 4*4
    area -= min(paper[2], 5) * 4
    paper[4] -= 1
    paper[2] = max(paper[2]-5, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[3]:
    area = 36 - 9 * min(paper[3], 4)
    if paper[3] >= 4:
        paper[3] -= 4
        area = 0
    elif paper[3] == 3:
        area -= min(1, paper[2]) * 4
        paper[3] -= 3
        paper[2] = max(paper[2]-1, 0)
    elif paper[3] == 2:
        area -= min(3, paper[2]) * 4
        paper[3] -= 2
        paper[2] = max(paper[2]-3, 0)
    else:
        area -= min(5, paper[2]) * 4
        paper[3] -= 1
        paper[2] = max(paper[2]-5, 0)

    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[2]:
    area = 36 - 4 * min(paper[2], 9)
    paper[2] = max(paper[2]-9, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[1]:
    paper[1] = max(paper[1]-36, 0)
    ans += 1

print(ans)
