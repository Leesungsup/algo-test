from collections import deque
def solution(numbers, hand):
    answer = ''
    k=[]
    Lx=0
    Ly=3
    Rx=2
    Ry=3
    map=[[0]*3 for _ in range(4)]
    #print(map)
    map[Ly][Lx]=1
    map[Ry][Rx]=1
    #print(map)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in numbers:
        if i==1 or i==4 or i==7:
            k.append('L')
            if i==1:
                Lx=0
                Ly=0
            elif i==4:
                Lx=0
                Ly=1
            else:
                Lx=0
                Ly=2
        elif i==3 or i==6 or i==9:
            k.append('R')
            if i==3:
                Rx=2
                Ry=0
            elif i==6:
                Rx=2
                Ry=1
            else:
                Rx=2
                Ry=2
        else:
            #print(i)
            if i==2:
                ex=1
                ey=0
            elif i==5:
                ex=1
                ey=1
            elif i==8:
                ex=1
                ey=2
            elif i==0:
                ex=1
                ey=3
            map=[[0]*3 for _ in range(4)]
            map[ey][ex]=1
            q=[]
            q=deque()
            q.append((Ly,Lx))
            Ltime=0
            time=0
            while q:
                #print(map)
                time+=1
                y,x=q.popleft()
                if Ltime!=0:
                    break
                for j in range(4):
                    nx=x+dx[j]
                    ny=y+dy[j]
                    if nx>=0 and nx<3 and ny>=0 and ny<4:
                        if map[ny][nx]==0:
                            map[ny][nx]=2
                            q.append((ny,nx))
                        elif map[ny][nx]==1:
                            Ltime=time
                            break
            #print(Ltime)
            map=[[0]*3 for _ in range(4)]
            map[ey][ex]=1
            q=[]
            q=deque()
            q.append((Ry,Rx))
            Rtime=0
            time=0
            while q:
                #print(map)
                time+=1
                y,x=q.popleft()
                if Rtime!=0:
                    break
                for j in range(4):
                    nx=x+dx[j]
                    ny=y+dy[j]
                    if nx>=0 and nx<3 and ny>=0 and ny<4:
                        if map[ny][nx]==0:
                            map[ny][nx]=2
                            q.append((ny,nx))
                        elif map[ny][nx]==1:
                            Rtime=time
                            break
            #print(Rtime)
            if Ltime<Rtime:
                Ly=ey
                Lx=ex
                k.append('L')
            elif Ltime==Rtime:
                if hand=='right':
                    Ry=ey
                    Rx=ex
                    k.append('R')
                else:
                    Ly=ey
                    Lx=ex
                    k.append('L')
            else:
                Ry=ey
                Rx=ex
                k.append('R')
    print(k)
    return answer
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
def solution1(numbers, hand):
    answer = ''
    # Keypad Coordinate: 0123456789*(10)#(11)
    distance = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]

    # initial position
    left = 10
    right = 11

    for i in numbers:
        # LEFT HAND
        if i in [1,4,7]:
            answer += 'L'
            left = i
        # RIGHT HAND
        elif i in [3,6,9]:
            answer += 'R'
            right = i
        # DISTACNE COMPARISON
        else:
            ldist = abs(distance[i][0] - distance[left][0]) + abs(distance[i][1] - distance[left][1])
            rdist = abs(distance[i][0] - distance[right][0]) + abs(distance[i][1] - distance[right][1])
            if ldist > rdist:
                answer += 'R'
                right = i
            elif ldist < rdist:
                answer += 'L'
                left = i
            # distance equals
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer
