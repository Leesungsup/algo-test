from collections import deque
def solution(grid):
    answer =[]
    len_x, len_y = len(grid),len(grid[0])
    visited = [[[0]*4 for _ in range(len_y)] for _ in range(len_x)]
    # D U L R
    move_dict = {0:(1,0),1:(-1,0),2:(0,-1),3:(0,1)}
    next_move_dict = {'S':{0:0,1:1,2:2,3:3},'L':{0:3,1:2,2:0,3:1},'R':{0:2,1:3,2:1,3:0}}
    for i in range(len_x):
        for j in range(len_y):
            while 0 in visited[i][j]:
                queue = deque()
                # do something
                idx = visited[i][j].index(0)
                # serach
                queue.append((i,j,idx,1,[i,j,idx]))
                visited[i][j][idx] = 1 # 해당 경로 방문처리
                while queue:
                    x, y, move, counting, first_move = queue.popleft()
                    df_x, df_y = move_dict[move]
                    x, y = x + df_x, y + df_y
                    if x == len_x:
                        x = 0
                    elif x < 0:
                        x = len_x-1
                    if y == len_y:
                        y = 0
                    elif y < 0:
                        y = len_y-1
                    next_idx = next_move_dict[grid[x][y]][move]
                    if [x,y,next_idx] == first_move:
                        answer.append(counting)
                    else:
                        visited[x][y][next_idx] = 1
                        queue.append((x,y,next_idx,counting+1,first_move))
    return sorted(answer)