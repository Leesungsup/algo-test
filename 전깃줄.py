n = int(input())
w = []
w_b = []
dp = [1 for i in range(n)]
for i in range(n):
    w.append(list(map(int, input().split())))
w.sort(key = lambda x:x[0])
for i in range(n):
    for j in range(i):
        if w[i][1] > w[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))

import sys

t = input()
for i in range(t):
    n = input()
    book1 = list(map(int, input().split()))
    m = input()
    book2 = list(map(int, input().split()))
    for j in book2:
        if j in book1:
            print('1')
        else:
            print('0')
