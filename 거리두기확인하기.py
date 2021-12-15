from collections import deque
def bfs(places,x,y):
    visit=[[] for _ in range(len(places[0]))]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    q.append((x,y,1))
    visit[x][y]=1
    while q:
        x,y,dist=q.popleft()
        if places[nx][ny]=='P' and 0<d<3:
            return False
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            d=dist+1
            if nx>=0 and nx<len(places) and ny>=0 and ny<len(places[0]):
                if places[nx][ny]!='X' and visit[nx][ny]:
                    q.append((nx,ny,d))
                    visit[nx][ny]=1
    return True
def solution(places):
    answer = []
    for i in places:
        chk=0
        for j in range(len(i)):
            for k in range(len(j[0])):
                if places[i][j]=='P':
                    if not bfs(places,i,j):
                        answer.append(0)
                        chk=1
                        break
                if chk==1:
                    break
            if chk==0:
                answer.append(1)
    return answer
