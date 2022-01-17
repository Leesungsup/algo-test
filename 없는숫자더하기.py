def solution(numbers):
    answer = -1
    a=[0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        a.remove(i)
    return sum(a)