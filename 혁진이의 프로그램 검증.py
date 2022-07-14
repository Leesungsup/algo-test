def solution(map1, visit, test, r, c):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    stack = [[0, 0, 3, 0]]
    while stack:
        x, y, d, m = stack.pop()
        if visit[x][y][d][m] == test:
            continue
        else:
            visit[x][y][d][m] = test
            if map1[x][y] == '<' or (map1[x][y] == '_' and m != 0):
                stack.append([(x + dx[1]) % r, (y + dy[1]) % c, 1, m])
            elif map1[x][y] == '>' or (map1[x][y] == '_' and m == 0):
                stack.append([(x + dx[3]) % r, (y + dy[3]) % c, 3, m])
            elif map1[x][y] == '^' or (map1[x][y] == '|' and m != 0):
                stack.append([(x + dx[0]) % r, (y + dy[0]) % c, 0, m])
            elif map1[x][y] == 'v' or (map1[x][y] == '|' and m == 0):
                stack.append([(x + dx[2]) % r, (y + dy[2]) % c, 2, m])
            elif map1[x][y] == '@':
                return True
            elif map1[x][y] == '+':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m + 1) % 16])
            elif map1[x][y] == '-':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m - 1) % 16])
            elif map1[x][y] == '.':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, m])
            elif map1[x][y] == '?':
                for i in range(4):
                    stack.append([(x + dx[i]) % r, (y + dy[i]) % c, i, m])
            else:
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, int(map1[x][y])])
    return False


t = int(input())
visit = [[[[0 for _ in range(16)] for _ in range(4)] for _ in range(20)] for _ in range(20)]
for test in range(1, t + 1):
    r, c = map(int, input().split())
    map1 = [input() for _ in range(r)]
    answer = solution(map1, visit, test, r, c)
    if answer==True:
        answer='YES'
    else:
        answer='NO'
    print('#{} {}'.format(test,answer))
