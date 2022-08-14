T = int(input())


def upGame(x, y):
    Y = y-1
    if 0 <= Y:
        if maps[Y][x] > 0:
            if maps[Y][x] == maps[y][x]:
                maps[Y][x] = maps[y][x] * 2
                maps[y][x] = -1
                return
            else:
                return
        elif maps[Y][x] == -1:
            maps[Y][x] = maps[y][x]
            maps[y][x] = 0
            return
        else:
            maps[Y][x] = maps[y][x]
            maps[y][x] = 0
            upGame(x, Y)


def downGame(x, y):
    Y = y+1
    if Y < N:
        if maps[Y][x] > 0:
            if maps[Y][x] == maps[y][x]:
                maps[Y][x] = maps[y][x] * 2
                maps[y][x] = -1
                return
            else:
                return

        elif maps[Y][x] == -1:
            maps[Y][x] = maps[y][x]
            maps[y][x] = 0
            return
        else:
            maps[Y][x] = maps[y][x]
            maps[y][x] = 0
            downGame(x, Y)


def rightGame(x, y):
    X = x + 1
    if X < N:
        if maps[y][X] > 0:
            if maps[y][X] == maps[y][x]:
                maps[y][X] = maps[y][x] * 2
                maps[y][x] = -1
                return
            else:
                return

        elif maps[y][X] == -1:
            maps[y][X] = maps[y][x]
            maps[y][x] = 0
            return
        else:
            maps[y][X] = maps[y][x]
            maps[y][x] = 0
            rightGame(X, y)


def leftGame(x, y):
    X = x - 1
    if 0 <= X:
        if maps[y][X] > 0:
            if maps[y][X] == maps[y][x]:
                maps[y][X] = maps[y][x] * 2
                maps[y][x] = -1
                return
            else:
                return

        elif maps[y][X] == -1:
            maps[y][X] = maps[y][x]
            maps[y][x] = 0
            return
        else:
            maps[y][X] = maps[y][x]
            maps[y][x] = 0
            leftGame(X, y)


for test_case in range(1, T+1):
    N, D = map(str, input().split())
    N = int(N)
    maps = []
    for n in range(N):
        maps.append(list(map(int, input().split())))

    if D == 'up':
        for y in range(N):
            for x in range(N):
                if maps[y][x]:
                    upGame(x, y)
    if D == 'down':
        for y in range(N-1, -1, -1):
            for x in range(N):
                if maps[y][x]:
                    downGame(x, y)
    if D == 'right':
        for x in range(N-1, -1, -1):
            for y in range(N):
                if maps[y][x]:
                    rightGame(x, y)
    if D == 'left':
        for x in range(N):
            for y in range(N):
                if maps[y][x]:
                    leftGame(x, y)
    for y in range(N):
        for x in range(N):
            if maps[y][x] == -1:
                maps[y][x] = 0

    print('#{}'.format(test_case))
    for i in range(N):
        print(' '.join(map(str, maps[i])))