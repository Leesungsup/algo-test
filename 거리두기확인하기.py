from collections import deque
def bfs(places,x,y):
    visit=[[0]*len(places) for _ in range(len(places))]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque()
    dist=0
    q.append((x,y,dist))
    visit[x][y]=1
    while q:
        x,y,dist=q.popleft()
        if places[x][y]=='P' and 0<dist<3:
            return False
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            d=dist+1
            if nx>=0 and nx<len(places) and ny>=0 and ny<len(places):
                if places[nx][ny]!='X' and visit[nx][ny]==0:
                    q.append((nx,ny,d))
                    visit[nx][ny]=1
    return True
def solution(places):
    answer = []
    number=0
    for i in places:
        chk=0
        number+=1
        for j in range(5):
            for k in range(5):
                if i[j][k]=='P':
                    if not bfs(i,j,k):
                        print(number)
                        answer.append(0)
                        chk=1
                        break
            if chk==1:
                break
        if chk==0:
            answer.append(1)
    print(answer)
    return answer
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
