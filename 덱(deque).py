from collections import deque
import sys
input=sys.stdin.readline
n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1
print(cnt)

input=sys.stdin.readline
d = deque()
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
            print(d[0])
            d.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
            print(d[len(d) - 1])
            d.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")