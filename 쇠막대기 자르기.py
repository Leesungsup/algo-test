T = int(input())
for test_case in range(1,T+1):
    arr = list(input())
    stick = 0
    answer = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(' and arr[i+1]==')':
            answer += stick
            i += 2
        elif arr[i] == '(':
            stick += 1
            i += 1
        else:
            answer += 1
            stick -= 1
            i += 1
    print('#{} {}'.format(test_case,answer))
