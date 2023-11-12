
#import sys
#sys.stdin = open("input.txt", "r")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def make_values_equal(A, B):
    if A == B:
        return 0

    diff = abs(A - B)
    if diff == 1 and (is_prime(A) or is_prime(B)):
        return 1
    elif diff % 2 == 0 or is_prime(diff):
        return 2
    else:
        return -1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''

    A, B = map(int, input().split())
    result = make_values_equal(A, B)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
