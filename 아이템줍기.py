from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0] * 101 for i in range(101)]
    cX = 2 * characterX
    cY = 2 * characterY
    iX = 2 * itemX
    iY = 2 * itemY
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[0] * 101 for i in range(101)]
    visited[cX][cY] = 1
    queue = deque([(cX, cY)])
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                board[i][j] = 1
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                board[i][j] = 0
    while queue:
        x, y = queue.popleft()
        if (x, y) == (iX, iY):
            print(board[x][y])
            answer = (board[x][y] - 1) // 2
            break
        for i in range(4):
            xTemp = x + dx[i]
            yTemp = y + dy[i]
            if 0 <= xTemp < 101 and 0 <= yTemp < 101 and board[xTemp][yTemp] != 0 and visited[xTemp][yTemp] == 0:
                board[xTemp][yTemp] = board[x][y] + 1
                visited[xTemp][yTemp] = 1
                queue.append((xTemp, yTemp))
    return answer
print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
