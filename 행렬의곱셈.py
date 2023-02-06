import sys
input=sys.stdin.readline
from itertools import combinations
def solution(arr1, arr2):
    answer = []
    print(answer)
    for k in range(len(arr1)):
        x_list=[]
        for i in range(len(arr2[0])):
            num=0
            for j in range(len(arr1[0])):
                print(arr1[k][j],arr2[j][i])
                num+=arr1[k][j]*arr2[j][i]
            x_list.append(num)
        answer.append(x_list)
    print(answer)
    return answer
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])


n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

array = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for c in range(m):
            array[i][j] += a[i][c] * b[c][j]

for i in array:
    for j in i:
        print(j, end = ' ')
    print()