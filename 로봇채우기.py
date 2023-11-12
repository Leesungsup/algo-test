import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1,0,0]
dy = [0,1,-1]

dp = [[[-1] * 4 for _ in range(m)] for _ in range(n)]


def go(x, y, z):

    if x == n - 1 and y == m - 1:
        return arr[x][y]

    if dp[x][y][z] != -1:
        return dp[x][y][z]

    dp[x][y][z] = -9876543210

    for i in range(3):
        # nx, ny : 다음 좌표
        nx, ny = x + dx[i], y + dy[i]

        if z == 1 and i == 2:
            continue
        if z == 2 and i == 1:
            continue

        if 0 <= nx < n and 0 <= ny < m:
            dp[x][y][z] = max(dp[x][y][z], go(nx, ny, i) + arr[x][y])
    return dp[x][y][z]

print(go(0,0,-1))
