

T=int(input())
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    arr=[[0]*n for _ in range(n)]
    b=0
    w=0
    if n==4:
        arr[1][1]='W'
        arr[1][2]='B'
        arr[2][1]='B'
        arr[2][2]='W'
    elif n==6:
        arr[2][2]='W'
        arr[2][3]='B'
        arr[3][2]='B'
        arr[3][3]='W'
    elif n==8:
        arr[3][3]='W'
        arr[3][4]='B'
        arr[4][3]='B'
        arr[4][4]='W'
    for i in range(m):
        x,y,g=map(int,input().split())
        x-=1
        y-=1
        if g==1:
            arr[x][y]='B'
            for k in range(n):
                if 0<=x+k<n and arr[x+k][y]=='B':
                    for j in range(x,x+k):
                        if arr[j][y]!=0:
                            arr[j][y]='B'
                        else:
                            break
                if 0<=x-k<n and arr[x-k][y]=='B':
                    for j in range(x,x-k,-1):
                        if arr[j][y]!=0:
                            arr[j][y]='B'
                        else:
                            break
                if 0<=y+k<n and arr[x][y+k]=='B':
                    for j in range(y,y+k):
                        if arr[x][j]!=0:
                            arr[x][j]='B'
                        else:
                            break
                if 0<=y-k<n and arr[x][y-k]=='B':
                    for j in range(y,y-k,-1):
                        if arr[x][j]!=0:
                            arr[x][j]='B'
                        else:
                            break
                if 0<=x+k<n and 0<=y+k<n and arr[x+k][y+k]=='B':
                    for j in range(k):
                        if arr[x+j][y+j]!=0:
                            arr[x+j][y+j]='B'
                        else:
                            break
                if 0<=x-k<n and 0<=y+k<n and arr[x-k][y+k]=='B':
                    for j in range(k):
                        if arr[x-j][y+j]!=0:
                            arr[x-j][y+j]='B'
                        else:
                            break
                if 0<=x+k<n and 0<=y-k<n and arr[x+k][y-k]=='B':
                    for j in range(k):
                        if arr[x+j][y-j]!=0:
                            arr[x+j][y-j]='B'
                        else:
                            break
                if 0<=x-k<n and 0<=y-k<n and arr[x-k][y-k]=='B':
                    for j in range(k):
                        if arr[x-j][y-j]!=0:
                            arr[x-j][y-j]='B'
                        else:
                            break
        elif g==2:
            arr[x][y]='W'
            for k in range(n):
                if 0<=x+k<n and arr[x+k][y]=='W':
                    for j in range(x,x+k):
                        if arr[j][y]!=0:
                            arr[j][y]='W'
                        else:
                            break
                if 0<=x-k<n and arr[x-k][y]=='W':
                    for j in range(x,x-k,-1):
                        if arr[j][y]!=0:
                            arr[j][y]='W'
                        else:
                            break
                if 0<=y+k<n and arr[x][y+k]=='W':
                    for j in range(y,y+k):
                        if arr[x][j]!=0:
                            arr[x][j]='W'
                        else:
                            break
                if 0<=y-k<n and arr[x][y-k]=='W':
                    for j in range(y,y-k,-1):
                        if arr[x][j]!=0:
                            arr[x][j]='W'
                        else:
                            break
                if 0<=x+k<n and 0<=y+k<n and arr[x+k][y+k]=='W':
                    for j in range(k):
                        if arr[x+j][y+j]!=0:
                            arr[x+j][y+j]='W'
                        else:
                            break
                if 0<=x+k<n and 0<=y-k<n and arr[x+k][y-k]=='W':
                    for j in range(k):
                        if arr[x+j][y-j]!=0:
                            arr[x+j][y-j]='W'
                        else:
                            break
                if 0<=x-k<n and 0<=y+k<n and arr[x-k][y+k]=='W':
                    for j in range(k):
                        if arr[x-j][y+j]!=0:
                            arr[x-j][y+j]='W'
                        else:
                            break
                if 0<=x-k<n and 0<=y-k<n and arr[x-k][y-k]=='W':
                    for j in range(k):
                        if arr[x-j][y-j]!=0:
                            arr[x-j][x-j]='W'
                        else:
                            break
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='B':
                b+=1
            elif arr[i][j]=='W':
                w+=1
    print("#{} {} {}".format(test_case,b,w))



T = int(input())
# 상, 하, 좌, 우 + 대각선 4개
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    t_N = int(N/2)
    arr[t_N-1][t_N] ,arr[t_N][t_N-1], arr[t_N-1][t_N-1] ,arr[t_N][t_N] = 1, 1, 2, 2
    for n in range(M):
        x, y, c = map(int, input().split())
        arr[y-1][x-1] = c
        for p in range(8):
            cnt = 0
            cx = x-1
            cy = y-1
            while cx+dx[p] >= 0 and cx+dx[p] < N and cy+dy[p] >= 0 and cy+dy[p] < N and arr[cy+dy[p]][cx+dx[p]]:
                if abs(arr[cy+dy[p]][cx+ dx[p]] - arr[y-1][x-1]) == 0:
                    for k in range(1, cnt+1):
                        cx = x-1
                        cy = y-1
                        arr[cy+dy[p]*k][cx+dx[p]*k] = c
                    break
                elif arr[cy+dy[p]][cx+dx[p]] != 0 and abs(arr[cy+dy[p]][cx+dx[p]] - arr[y-1][x-1]) == 1:
                    cnt += 1
                    cy += dy[p]
                    cx += dx[p]
    sum_w = 0
    sum_b = 0
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if arr[j][i] == 1:
                sum_b += 1
            elif arr[j][i] == 2:
                sum_w += 1
    print('#{} {} {}'.format(t, sum_b, sum_w))
