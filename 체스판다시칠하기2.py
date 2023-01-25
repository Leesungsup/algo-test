import sys
input = sys.stdin.readline

n,m=map(int,input().split())

mtr=[]
cnt=[]
for i in range(n):
    mtr.append(input())

for a in range(n-7):
    for b in range(m-7):
        w_index=0
        b_index=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if mtr[i][j]!='W':
                        w_index+=1
                    else:
                        b_index+=1
                else:
                    if mtr[i][j]!='W':
                        b_index+=1
                    else:
                        w_index+=1

        cnt.append(w_index)
        cnt.append(b_index)
print(min(cnt))

n, m, k = map(int, input().split())
board = [[0]*m] + [[0] + list(input().strip()) for _ in range(n)]
check_W = ["0"*(m+1)] + ["0" + "WB"*(m//2) + "W"*(m%2), "0" + "BW"*(m//2) + "B"*(m%2)]*(n//2) + ["0" + "WB"*(m//2) + "W"*(m%2)]*(n%2)
check_B = ["0"*(m+1)] + ["0" + "BW"*(m//2) + "B"*(m%2), "0" + "WB"*(m//2) + "W"*(m%2)]*(n//2) + ["0" + "BW"*(m//2) + "B"*(m%2)]*(n%2)
sum_sub_W = [[0]*(m+1) for _ in range(n+1)]
sum_sub_B = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        sum_sub_W[i][j] = int(board[i][j] != check_W[i][j]) + sum_sub_W[i-1][j] + sum_sub_W[i][j-1] - sum_sub_W[i-1][j-1]
        sum_sub_B[i][j] = int(board[i][j] != check_B[i][j]) + sum_sub_B[i-1][j] + sum_sub_B[i][j-1] - sum_sub_B[i-1][j-1]

result = float("inf")
for x_start in range(1, n-k+2):
    for y_start in range(1, m-k+2):
        x_point = x_start+k-1
        y_point = y_start+k-1

        cnt_color_W = sum_sub_W[x_point][y_point] - sum_sub_W[x_start-1][y_point] - sum_sub_W[x_point][y_start-1] + sum_sub_W[x_start-1][y_start-1]
        cnt_color_B = sum_sub_B[x_point][y_point] - sum_sub_B[x_start-1][y_point] - sum_sub_B[x_point][y_start-1] + sum_sub_B[x_start-1][y_start-1]

        result = min(result, cnt_color_W, cnt_color_B)

print(result)