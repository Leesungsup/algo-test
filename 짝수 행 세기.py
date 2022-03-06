def solution(a):
    MOD = 10 ** 7 + 19
    R, C = len(a), len(a[0])
    pascal = [[0] * (R + 1) for _ in range(R + 1)]
    def comb(n, c):
        if n == c or c == 0:
            pascal[n][c] = 1
            return 1
        if pascal[n][c] > 0:
            return pascal[n][c] % MOD
        pascal[n][c] = (comb(n - 1, c - 1) + comb(n - 1, c)) % MOD
        return pascal[n][c]
    for i in range(R + 1):
        for j in range(i + 1):
            comb(i, j)
    cnt = []
    for j in range(C):
        o = 0
        for i in range(R):
            if a[i][j] == 1:
                o += 1
        cnt.append(o)
solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])
