import sys
input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort()

for num in arr:
    lt, rt = 0, n - 1
    answer = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == a[mid]:
            answer = True
            print(1)
            break
        elif num > a[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not answer:
        print(0)