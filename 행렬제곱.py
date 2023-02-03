import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def mulMatrix(m1, m2):
    tmpArr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += m1[i][k] * m2[k][j] % 1000
            tmpArr[i].append(tmp)
    return tmpArr

def squareMatrix(b):
    if b == 1:
        return matrix
    result = squareMatrix(b//2)
    squareResult = mulMatrix(result, result)
    if b % 2 == 0:
        return squareResult
    else:
        return mulMatrix(squareResult, matrix)

for ans in squareMatrix(b):
    for a in ans:
        print(a % 1000, end=" ")
    print()