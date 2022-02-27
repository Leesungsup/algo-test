def solution(land, P, Q):
    lst = []
    for i in land:
        lst += i
        print(i)
    lst = sorted(lst)
    print(lst)
    n = len(lst)
    #모두제거
    answer = sum(lst)*Q
    #맨밑으로제거
    cost = (sum(lst) - lst[0]*n )*Q
    answer = min(answer, cost)

    for i in range(1, n):
        if lst[i] != lst[i-1]:
            #추가 + 복원
            cost += (P * i * (lst[i]-lst[i-1])) - (Q * (n-i) * (lst[i]-lst[i-1]))
            answer = min(answer, cost)

    return answer
solution([[1, 2], [2, 3]],3,2)
