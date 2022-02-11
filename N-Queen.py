arr=[[]*12 for _ in range(12)]
print(arr)
def able(x,y):
    for i in range(n):
        if arr[i][y]==1:
            ret_num=0
    for j in range(n):
        if arr[x][j]==1:
            ret_num=0
    if x>=y:
        for i in range(n):
            for j in range(n):
                if i-j == x-y:
                    if arr[i][j]==1:
                        ret_num=0
    else:
        for i in range(n):
            for j in range(n):
                if j-i==y-x:
                    if arr[i][j]==1:
                        ret_num=0
    for i in range(n):
        for j in range(n):
            if i+j==x+y:
                if arr[i][j]==1:
                    ret_num=0
    return ret_num
def solution(n):
    answer = 0
    def check(depth):
        if depth==n:
            answer+=1
        for i in range(n):
            if able(i,depth)==1:
                arr[i][depth]=1
                check(depth+1)
            arr[i][depth]=0
    return answer
def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count
def solution1(n):
    return dfs([0]*n, 0, n)
solution1(4)