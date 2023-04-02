import sys
from collections import Counter


n, m = map(int, sys.stdin.readline().split())
woods = Counter(map(int, sys.stdin.read().split())).items()
s, e = 0, max(woods)[0]
answer = 0
while s <= e:
    mid = s + (e - s) // 2
    if sum([(wood - mid) * c if wood > mid else 0 for wood, c in woods]) >= m:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1
print(answer)

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end:
    mid = (start+end) // 2

    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid


    if log >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)