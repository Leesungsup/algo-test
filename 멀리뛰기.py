from itertools import permutations
def solution(n):
    answer = 0
    candidates=[1,2]
    result=[]
    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(n, 0, [])
    print(result)
    for i in result:
        print(i.count(1))
        if i.count(1)!=0 and i.count(2)!=0:
            for j in map(list,permutations(i,len(i))):
                if j not in result:
                    result.append(j)
    print(result)
    return len(result)
solution(4)
def solution1(n):
    arr=[1,1]
    for i in range(2,n+1):
        print(i,arr[i-1],arr[i-2])
        arr.append(arr[i-1]+arr[i-2])
    print(arr)
    print(arr[n])
    return arr[n]%1234567
solution1(8)
