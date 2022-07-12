import sys
sys.stdin = open("input.txt", "r")
T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,count):
    global n,ma,cx,cy,c
    ma=max(ma,count)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if arr[nx][ny]==arr[x][y]+1:
                dfs(nx,ny,count+1)
for test_case in range(1,T+1):
    n=int(input())
    arr=[]
    ma=0
    count=1
    max_move=0
    room_num=999999999
    mi=dict()
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            ma=0
            dfs(i,j,1)
            if max_move < ma:
                room_num = arr[i][j]
                max_move = ma
            elif max_move == ma:  # 저장되어 있는 최대 이동 횟수와 이동 횟수가 같다면 방 번호 더 작은걸로 갱신
                room_num = min(room_num, arr[i][j])
    print("#{} {} {}".format(test_case,room_num,max_move))
