n=int(input())
a=[]
b=[[0]*n for _ in range(n)]
print(b)
# for i in range(n):
#     a.append(list(map(int,input().split())))
print(a)
sw=-1
w=1
h=1
count=1
c=int((n-1)/2)
r=int((n-1)/2)
sum=0
while True:
    for i in range(w):
        print(c,r)
        if sw==-1:
            if c+1>=n:
                sum+=int(a[c][r]*0.07)
            else:
                a[c+1][r]+=int(a[c][r]*0.07)
            if c-1<0:
                sum+=int(a[c][r]*0.07)
            else:
                a[c-1][r]+=int(a[c][r]*0.07)
            if c+2>=n:
                sum+=int(a[c][r]*0.02)
            else:
                a[c+2][r]+=int(a[c][r]*0.02)
            if c-2<0:
                sum+=int(a[c][r]*0.02)
            else:
                a[c-2][r]+=int(a[c][r]*0.02)
            if c-1<0 or r-1<0:
                sum+=int(a[c][r]*0.1)
            else:
                a[c-1][r-1]+=int(a[c][r]*0.1)
            if c+1>=n or r-1<0:
                sum+=int(a[c][r]*0.1)
            else:
                a[c+1][r-1]+=int(a[c][r]*0.1)
            if c-1<0 or r+1>=n:
                sum+=int(a[c][r]*0.01)
            else:
                a[c-1][r+1]+=int(a[c][r]*0.01)
            if c+1>=n or r+1>=n:
                sum+=int(a[c][r]*0.01)
            else:
                a[c+1][r+1]+=int(a[c][r]*0.01)
            if r-2<0:
                sum+=int(a[c][r]*0.05)
            else:
                a[c][r-2]+=int(a[c][r]*0.05)
            num=int(a[c][r]*0.45)
            if r+1>=n:
                sum+=(a[c][r]-num)
            else:
                a[c][r+1]+=(a[c][r]-num)
            a[c][r]=0
        else:
            a[c+1][r]+=int(a[c][r]*0.07)
            a[c-1][r]+=int(a[c][r]*0.07)
            a[c+2][r]+=int(a[c][r]*0.02)
            a[c-2][r]+=int(a[c][r]*0.02)
            a[c-1][r-1]+=int(a[c][r]*0.01)
            a[c+1][r-1]+=int(a[c][r]*0.01)
            a[c-1][r+1]+=int(a[c][r]*0.1)
            a[c+1][r+1]+=int(a[c][r]*0.1)
            a[c][r+2]+=int(a[c][r]*0.05)
            num=int(a[c][r]*0.45)
            a[c][r-1]+=(a[c][r]-num)
            a[c][r]=0

        b[c][r]=count
        r+=sw
        count+=1
    if count> n*n:
        break
    sw*=-1
    for i in range(h):
        b[c][r]=count
        c+=sw
        count+=1
    w+=1
    h+=1
for i in range(n):
    print(b[i])


def recount(s_x, s_y, direction):
    global ans

    if s_y < 0:
        return

    total = 0
    for dx, dy, z in direction:
        nx = s_x + dx
        ny = s_y + dy
        if z == 0:
            new_sand = sand[s_x][s_y] - total
        else:
            new_sand = int(sand[s_x][s_y] * z)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            sand[nx][ny] += new_sand
        else:
            ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]


left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

s_x, s_y = N//2, N//2
ans = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

dict = {0: left, 1: down, 2: right, 3: up}
time = 0
for i in range(2*N-1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        recount(n_x, n_y, dict[d])
        s_x, s_y = n_x, n_y

print(ans)