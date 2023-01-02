# import sys
#
# N, R = map(int, sys.stdin.readline().split())
#
# def dp(num):
#     arr = {}
#     if num in arr:
#         return arr[num]
#     elif num == 0 or num == 1:
#         arr[num] = 1
#         return 1
#     else:
#         factorial = num * dp(num - 1)
#         arr[num] = factorial
#     return factorial
#
# ans = dp(N) // (dp(R) * dp(N - R))
# print(ans)


# l = ['a', 'b', 'c', 'd']
# n = len(l)
# r = 2
# answer = []
#
# def dfs(idx, list):
#     if len(list) == r:
#         answer.append(list[:])
#         return
#
#     for i in range(idx, n):
#         dfs(i+1,list+[l[i]])
#
# dfs(0, [])
# print(answer)

l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0


dfs(0, [])
print(answer)

def choose(n,k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)

print(choose(10,2))