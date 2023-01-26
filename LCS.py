import sys
input=sys.stdin.readline
sys.setrecursionlimit(3000)
a = input().strip()
b = input().strip()
lcs = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
print(lcs[-1][-1])

i=len(a)
j=len(b)
ans = ""
while i>0 and j>0:
    if lcs[i][j] == lcs[i][j-1]:
        j-=1
    elif lcs[i][j] == lcs[i-1][j]:
        i-=1
    else:
        ans = a[i-1] + ans
        i-=1
        j-=1
if ans:
    print(ans)